from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Cookie Handling</h1><p>Django program implementation</p>')
