from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Photomodel,Commentmodel
from user_app.models import UserModel
from .forms import Photoform,Commentform
# Create your views here.
def index(request):
    if 'id' in request.session:
        photos = Photomodel.objects.all()
        data = []
        for photo in photos:
            two_comments = Commentmodel.objects.filter(parent_post=photo)[:2]
            d = {
                'photo': photo,
                'comments': two_comments
            }
            data.append(d)
        context = {
            'posts': data
        }
        return render(request, 'photo_app/index.html', context)


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
 
def profile(request):
    if 'id' in request.session:
        user_id = request.session['id']
        photos = Photomodel.objects.filter(User = user_id)
        user = UserModel.objects.filter(id = user_id)
        dict = {'upload':photos,'user':user}
        # data = []
        # for photo in photos:
        #     two_comments = Commentmodel.objects.filter(parent_post=photo)[:2]
        #     d = {
        #         'photo': photo,
        #         'comments': two_comments
        #     }
        #     data.append(d)
        # context = {
        #     'posts': data
        # }
        # return render(request, 'photo_app/index.html', context)
        return render(request, 'photo_app/profile.html',dict)

    else:
        return redirect('user:login')
    
def delete(request,id):
    photo = Photomodel.objects.get(id=id)
    photo.delete()
    return redirect('photo_app:profile')