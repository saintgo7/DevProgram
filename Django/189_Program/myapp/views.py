from django.http import HttpResponse

def index(request):
    return HttpResponse('Django Program 189')