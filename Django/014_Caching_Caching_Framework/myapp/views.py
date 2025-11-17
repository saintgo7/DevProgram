from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Caching Framework</h1><p>Django program implementation</p>')
