from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Email Sending</h1><p>Django program implementation</p>')
