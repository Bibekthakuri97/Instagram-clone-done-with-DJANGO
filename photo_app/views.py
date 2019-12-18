from django.shortcuts import render
from django.http import HttpResponse
from .models import Photomodel,Commentmodel
# Create your views here.
def index(request):
    upload = Photomodel.objects.all()
    comupload = Commentmodel.objects.all()


    return render(request, 'photo_app\index.html',{'upload':upload,'comupload':comupload})
    #return HttpResponse('Hello world')