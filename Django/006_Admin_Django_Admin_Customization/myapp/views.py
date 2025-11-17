from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Django Admin Customization</h1><p>Django program implementation</p>')
