from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Django Program 53</h1><p>Django program implementation</p>')
