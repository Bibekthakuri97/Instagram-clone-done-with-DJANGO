from django.shortcuts import render
from django.http import HttpResponse
from .models import Photomodel
# Create your views here.
def index(request):
    upload = Photomodel.objects.all()


    return render(request, 'photo_app\index.html',{'upload':upload})
    #return HttpResponse('Hello world')