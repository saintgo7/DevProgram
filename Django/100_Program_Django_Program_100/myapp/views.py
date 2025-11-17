from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Django Program 100</h1><p>Django program implementation</p>')
