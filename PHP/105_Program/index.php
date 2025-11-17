<?php
/**
 * Laravel Eloquent ORM Examples
 */

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * User Model
 */
class User extends Model
{
    use SoftDeletes;

    protected $fillable = ['name', 'email', 'password'];
    protected $hidden = ['password', 'remember_token'];
    protected $casts = [
        'email_verified_at' => 'datetime',
        'is_admin' => 'boolean',
    ];

    // Relationships
    public function posts()
    {
        return $this->hasMany(Post::class);
    }

    public function profile()
    {
        return $this->hasOne(Profile::class);
    }

    public function roles()
    {
        return $this->belongsToMany(Role::class);
    }

    // Scopes
    public function scopeActive($query)
    {
        return $query->where('active', true);
    }

    public function scopeAdmin($query)
    {
        return $query->where('is_admin', true);
    }

    // Accessors & Mutators
    public function getFullNameAttribute()
    {
        return "{$this->first_name} {$this->last_name}";
    }

    public function setPasswordAttribute($value)
    {
        $this->attributes['password'] = bcrypt($value);
    }
}

/**
 * Post Model
 */
class Post extends Model
{
    protected $fillable = ['title', 'content', 'user_id', 'published_at'];
    protected $casts = [
        'published_at' => 'datetime',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function comments()
    {
        return $this->hasMany(Comment::class);
    }

    public function tags()
    {
        return $this->belongsToMany(Tag::class);
    }

    public function scopePublished($query)
    {
        return $query->whereNotNull('published_at')
                    ->where('published_at', '<=', now());
    }
}

/**
 * Usage Examples
 */

// CREATE
$user = User::create([
    'name' => 'John Doe',
    'email' => 'john@example.com',
    'password' => 'secret123'
]);

// READ
$users = User::all();
$user = User::find(1);
$user = User::where('email', 'john@example.com')->first();
$users = User::where('active', true)->get();

// UPDATE
$user = User::find(1);
$user->name = 'Jane Doe';
$user->save();

// Or mass update
User::where('active', false)->update(['active' => true]);

// DELETE
$user = User::find(1);
$user->delete();

// Soft delete
$user->delete(); // Soft deletes
$user->forceDelete(); // Permanently delete
$users = User::withTrashed()->get(); // Include soft deleted
$user->restore(); // Restore soft deleted

// RELATIONSHIPS
$user = User::with('posts')->find(1);
$posts = $user->posts;

$post = Post::with('user', 'comments')->find(1);
$author = $post->user->name;

// QUERIES
$users = User::active()->admin()->get();
$posts = Post::published()->with('user')->latest()->paginate(15);

$users = User::whereHas('posts', function($query) {
    $query->where('published', true);
})->get();

// AGGREGATES
$count = User::count();
$max = User::max('id');
$avg = Post::avg('views');

// RAW QUERIES
$users = User::whereRaw('age > ?', [18])->get();
$users = User::select('name', 'email')
             ->selectRaw('count(*) as post_count')
             ->join('posts', 'users.id', '=', 'posts.user_id')
             ->groupBy('users.id')
             ->get();
?>
