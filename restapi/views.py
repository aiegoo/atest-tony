from django.shortcuts import render

# Create your views here.
def home(request):
     return httpResponse("hello, Django")

def taskstring(request):
     result = 'Rest API string! got your link now'
     return HttpResponse(result, content_type="text/plain")