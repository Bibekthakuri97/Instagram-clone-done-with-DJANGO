from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserModel

# Create your views here.
def display(request):
    return render(request, 'user_app/display.html')

def logout(request):
    request.session.flush()
    return redirect('user:login')

def loginauth(request):

    if request.method == "POST":
        e = request.POST.get('email')
        pw = request.POST.get('pass')

        user = UserModel.objects.filter(email=e,passwrod=pw)

        if(user.count()>0):
            for user in user:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['username'] = user.username
                return redirect('photo_app:index')

        else:
            return HttpResponse('Milenaaaaa')

    else:    
        return render(request, 'user_app/login.html')
# Create your views here.
