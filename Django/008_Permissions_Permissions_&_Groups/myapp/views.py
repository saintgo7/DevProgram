from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Permissions & Groups</h1><p>Django program implementation</p>')
