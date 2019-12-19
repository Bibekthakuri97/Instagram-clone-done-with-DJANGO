from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Photomodel,Commentmodel
from .forms import Photoform,Commentform
# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = Photomodel.objects.all()
        comupload = Commentmodel.objects.all()
        return render(request, 'photo_app/index.html',{'upload':upload,'comupload':comupload})
    else:
        return redirect('user:login')
    #return HttpResponse('Hello world')

def add(request):
    if request.method == "POST":
        form = Photoform(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('you have failed looser.')

        else:
            print(form.errors)
            return HttpResponse('Form not valid')
    else:
        form = Photoform
        return render(request,'photo_app/addphoto.html',{'form':form})
 
def edit(request,id):
    photo = Photomodel.objects.get(id=id) #get gives error us filter doesnt, get is used insted of filter
    if request.method == "POST":
        form = Photoform(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('you have failed looser.')

        else:
            print(form.errors)
            return HttpResponse('Form not valid')
    else:
        form = Photoform
        return render(request,'photo_app/editphoto.html',{'photo':photo})
 