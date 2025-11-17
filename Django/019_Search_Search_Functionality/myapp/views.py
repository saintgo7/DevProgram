from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Search Functionality</h1><p>Django program implementation</p>')
