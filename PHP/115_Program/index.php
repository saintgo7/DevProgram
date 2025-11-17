<?php
/**
 * Laravel Middleware Examples
 */

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

/**
 * Check if user is admin
 */
class CheckAdmin
{
    public function handle(Request $request, Closure $next)
    {
        if (!auth()->check() || !auth()->user()->is_admin) {
            abort(403, 'Unauthorized action.');
        }

        return $next($request);
    }
}

/**
 * Log all requests
 */
class LogRequests
{
    public function handle(Request $request, Closure $next)
    {
        \Log::info('Request', [
            'method' => $request->method(),
            'url' => $request->fullUrl(),
            'ip' => $request->ip(),
            'user_id' => auth()->id(),
        ]);

        return $next($request);
    }
}

/**
 * Check API token
 */
class CheckApiToken
{
    public function handle(Request $request, Closure $next)
    {
        $token = $request->header('X-API-Token');

        if (!$token || !$this->isValidToken($token)) {
            return response()->json(['error' => 'Invalid API token'], 401);
        }

        return $next($request);
    }

    private function isValidToken($token)
    {
        // Validate token logic
        return $token === config('app.api_token');
    }
}

/**
 * Rate limiting middleware
 */
class ThrottleRequests
{
    public function handle(Request $request, Closure $next, $maxAttempts = 60, $decayMinutes = 1)
    {
        $key = $this->resolveRequestSignature($request);

        if ($this->tooManyAttempts($key, $maxAttempts)) {
            return response()->json([
                'error' => 'Too many requests'
            ], 429);
        }

        $this->hit($key, $decayMinutes * 60);

        return $next($request);
    }

    protected function resolveRequestSignature($request)
    {
        return sha1($request->ip() . '|' . $request->fullUrl());
    }

    protected function tooManyAttempts($key, $maxAttempts)
    {
        return \Cache::get($key, 0) >= $maxAttempts;
    }

    protected function hit($key, $decaySeconds)
    {
        \Cache::put($key, \Cache::get($key, 0) + 1, $decaySeconds);
    }
}

/**
 * Register middleware in app/Http/Kernel.php
 */
class Kernel extends HttpKernel
{
    protected $middleware = [
        // Global middleware
        \App\Http\Middleware\LogRequests::class,
    ];

    protected $middlewareGroups = [
        'web' => [
            // Web middleware group
        ],

        'api' => [
            'throttle:api',
            \App\Http\Middleware\CheckApiToken::class,
        ],
    ];

    protected $routeMiddleware = [
        'admin' => \App\Http\Middleware\CheckAdmin::class,
        'throttle.custom' => \App\Http\Middleware\ThrottleRequests::class,
    ];
}

/**
 * Usage in routes
 */

// Single middleware
Route::get('/admin/dashboard', function () {
    //
})->middleware('admin');

// Multiple middleware
Route::middleware(['auth', 'admin'])->group(function () {
    Route::get('/admin/users', [UserController::class, 'index']);
});

// Middleware with parameters
Route::middleware('throttle.custom:10,1')->group(function () {
    Route::post('/api/data', [ApiController::class, 'store']);
});
?>
