from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Custom Middleware</h1><p>Django program implementation</p>')
