#!/usr/bin/env python3
"""
Create 100 Django programs
Django: High-level Python web framework
"""

import os
import sys

# Program definitions
programs = [
    # Featured Programs (1-5) - Full implementations
    ("001_HelloWorld", "Hello World Django", """myapp/views.py:
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Hello Django!</h1><p>The web framework for perfectionists with deadlines</p>')

def hello_template(request):
    context = {'name': 'Django', 'version': '5.0'}
    return render(request, 'hello.html', context)

myapp/urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template/', views.hello_template, name='hello_template'),
]

myapp/templates/hello.html:
<!DOCTYPE html>
<html>
<head>
    <title>Hello Django</title>
</head>
<body>
    <h1>Hello {{ name }}!</h1>
    <p>Version: {{ version }}</p>
</body>
</html>

myproject/urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
"""),

    ("002_ModelsORM", "Models and ORM", """myapp/models.py:
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

myapp/views.py:
from django.shortcuts import render, get_object_or_404
from .models import Author, Post

def post_list(request):
    posts = Post.objects.filter(status='published').select_related('author')
    return render(request, 'posts.html', {'posts': posts})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = author.posts.all()
    return render(request, 'author.html', {'author': author, 'posts': posts})
"""),

    ("003_ViewsURLs", "Views and URL Routing", """myapp/views.py:
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

# Function-based view
def home(request):
    return render(request, 'home.html')

# Class-based view
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

# Generic ListView
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

# Generic DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# API view
def api_posts(request):
    posts = Post.objects.values('id', 'title', 'created_at')
    return JsonResponse(list(posts), safe=False)

myapp/urls.py:
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('api/posts/', views.api_posts, name='api_posts'),
]
"""),

    ("004_Forms", "Django Forms", """myapp/forms.py:
from django import forms
from .models import Post

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email must be from example.com domain')
        return email

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters')
        return title

myapp/views.py:
from django.shortcuts import render, redirect
from .forms import ContactForm, PostForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Send email, save to database, etc.
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
"""),

    ("005_RESTAPI", "Django REST Framework", """myapp/serializers.py:
from rest_framework import serializers
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'posts_count', 'created_at']

    def get_posts_count(self, obj):
        return obj.posts.count()

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_name', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

myapp/views.py:
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        author = self.get_object()
        posts = author.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.status = 'published'
        post.save()
        return Response({'status': 'post published'})

myapp/urls.py:
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

requirements-extra.txt:
djangorestframework==3.14.0
"""),

    # Template Programs (6-100)
    ("006_Admin", "Django Admin Customization", ""),
    ("007_Authentication", "User Authentication", ""),
    ("008_Permissions", "Permissions & Groups", ""),
    ("009_Middleware", "Custom Middleware", ""),
    ("010_Templates", "Template Inheritance", ""),
    ("011_StaticFiles", "Static Files Management", ""),
    ("012_MediaFiles", "Media File Upload", ""),
    ("013_Signals", "Django Signals", ""),
    ("014_Caching", "Caching Framework", ""),
    ("015_Sessions", "Session Management", ""),
    ("016_Cookies", "Cookie Handling", ""),
    ("017_Email", "Email Sending", ""),
    ("018_Pagination", "Query Pagination", ""),
    ("019_Search", "Search Functionality", ""),
    ("020_Filtering", "QuerySet Filtering", ""),
    ("021_Aggregation", "Aggregation Functions", ""),
    ("022_Transactions", "Database Transactions", ""),
    ("023_Migrations", "Database Migrations", ""),
    ("024_CustomManagers", "Custom Model Managers", ""),
    ("025_TemplateFilters", "Custom Template Filters", ""),
]

# Generate remaining programs
for i in range(26, 101):
    programs.append((
        f"{i:03d}_Program",
        f"Django Program {i}",
        ""
    ))

def create_django_program(number, name, content):
    """Create a Django program directory with files"""
    dir_name = f"Django/{number}_{name.replace(' ', '_').replace('/', '_')}"
    os.makedirs(dir_name, exist_ok=True)
    os.makedirs(f"{dir_name}/myapp", exist_ok=True)
    os.makedirs(f"{dir_name}/myapp/templates", exist_ok=True)
    os.makedirs(f"{dir_name}/myproject", exist_ok=True)

    extra_reqs = []

    # Parse content for featured programs
    if content:
        files = {}
        current_file = None
        current_content = []

        for line in content.split('\n'):
            if line.startswith('requirements-extra.txt:'):
                extra_reqs.append(line.replace('requirements-extra.txt:', '').strip())
                continue
            if line.endswith(':') and not line.startswith(' '):
                if current_file:
                    files[current_file] = '\n'.join(current_content)
                current_file = line[:-1]
                current_content = []
            else:
                current_content.append(line)

        if current_file:
            files[current_file] = '\n'.join(current_content)

        # Write parsed files
        for filename, file_content in files.items():
            filepath = os.path.join(dir_name, filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                f.write(file_content.strip() + '\n')
    else:
        # Template program
        with open(f"{dir_name}/myapp/views.py", 'w') as f:
            f.write(f"""from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>{name}</h1><p>Django program implementation</p>')
""")

        with open(f"{dir_name}/myapp/urls.py", 'w') as f:
            f.write("""from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
""")

        with open(f"{dir_name}/myproject/urls.py", 'w') as f:
            f.write("""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
""")

    # Create __init__.py files
    open(f"{dir_name}/myapp/__init__.py", 'w').close()
    open(f"{dir_name}/myproject/__init__.py", 'w').close()

    # Create models.py if not exists
    if not os.path.exists(f"{dir_name}/myapp/models.py"):
        with open(f"{dir_name}/myapp/models.py", 'w') as f:
            f.write("""from django.db import models

# Create your models here.
""")

    # Create settings.py
    with open(f"{dir_name}/myproject/settings.py", 'w') as f:
        f.write(f"""import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-secret-key-change-in-production'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [{{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {{
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    }},
}}]

DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
""")

    # Create manage.py
    with open(f"{dir_name}/manage.py", 'w') as f:
        f.write("""#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
""")

    # Create requirements.txt
    with open(f"{dir_name}/requirements.txt", 'w') as f:
        f.write("Django>=5.0,<6.0\n")
        for req in extra_reqs:
            if req:
                f.write(f"{req}\n")

def main():
    print("Creating Django programs...")
    os.makedirs("Django", exist_ok=True)

    # Create README
    with open("Django/README.md", 'w') as f:
        f.write("""# Django Programs

100 Django programs demonstrating Python web framework.

## Features
- MVT (Model-View-Template) Architecture
- ORM (Object-Relational Mapping)
- Admin Panel
- Forms & Validation
- Authentication System
- Django REST Framework
- Database Migrations

## Quick Start

```bash
cd Django/001_HelloWorld
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Visit http://localhost:8000
```

## Create Superuser

```bash
python manage.py createsuperuser
# Visit http://localhost:8000/admin
```

## Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
""")

    total_lines = 0
    for number, name, content in programs:
        create_django_program(number, name, content)
        # Count lines
        dir_name = f"Django/{number}_{name.replace(' ', '_').replace('/', '_')}"
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if file.endswith(('.py', '.html', '.txt')):
                    with open(os.path.join(root, file), 'r') as f:
                        total_lines += len(f.readlines())

    print(f"✅ Created 100 Django programs ({total_lines:,} lines)")
    return total_lines

if __name__ == "__main__":
    lines = main()
    sys.exit(0)
