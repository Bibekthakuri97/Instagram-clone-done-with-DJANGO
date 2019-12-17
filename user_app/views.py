from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return render(request, 'user_app\display.html')


# Create your views here.
