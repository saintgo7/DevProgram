from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Database Transactions</h1><p>Django program implementation</p>')
