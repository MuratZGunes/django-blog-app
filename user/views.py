from django.shortcuts import render,redirect # Django'nun redirect fonksiyonunu import ettik
from .forms import RegisterForm,LoginForm # forms.py dosyasındaki RegisterForm classını import ettik

from django.contrib.auth.models import User # Django'nun default user modelini import ettik
from django.contrib.auth import login,authenticate,logout     # Django'nun login fonksiyonunu import ettik

from django.contrib import messages # Django'nun messages frameworkünü import ettik
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None) # formu oluşturduk
    if form.is_valid():                     # formun doğru olup olmadığını kontrol ettik
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')
            
            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)  # kullanıcıyı oturum açtık
            messages.success(request,'Başarıyla kayıt oldunuz')

            return redirect('index')    

    context = {         # formun doğru olmadığı durumda formu tekrar göstermek için context oluşturduk  isvalidi geçemezse
            'form':form
        }
    return render(request,'register.html',context)
    

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        'form':form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username = username,password = password)
        
        if user is None:
            messages.info(request,'Kullanıcı adı veya şifre hatalı')
            return render(request,'login.html',context)

        messages.success(request,'Başarıyla giriş yaptınız')
        login(request,user)
        return redirect('index')

    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla çıkış yaptınız')
    return redirect('index')