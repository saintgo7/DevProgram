from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>User Authentication</h1><p>Django program implementation</p>')
