from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!!')

def callTest(request):
    msg = 'My Message'
    title = 'My FirstTest'
    return render(request, './exam1/ctIndex.html', {'message':msg, 'myTitle': title })