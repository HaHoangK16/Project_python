from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello app")
    return render(request, 'pages/home_page01.html')
