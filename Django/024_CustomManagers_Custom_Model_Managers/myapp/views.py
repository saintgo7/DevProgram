from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Custom Model Managers</h1><p>Django program implementation</p>')
