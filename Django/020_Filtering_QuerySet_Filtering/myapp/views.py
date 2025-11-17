from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>QuerySet Filtering</h1><p>Django program implementation</p>')
