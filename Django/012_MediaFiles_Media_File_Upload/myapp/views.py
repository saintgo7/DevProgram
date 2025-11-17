from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Media File Upload</h1><p>Django program implementation</p>')
