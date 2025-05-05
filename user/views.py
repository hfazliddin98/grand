from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.models import User
from user.forms import KirishForm, RoyhatForm


def home(request):

    return render(request, 'asosiy/home.html')

def kirish(request):
    if request.method == 'POST':
        form = KirishForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # yoki istalgan sahifaga yo‘naltirish
            else:
                form.add_error(None, 'Login yoki parol noto‘g‘ri')
    else:
        form = KirishForm()

    contex = {
        'form':form
    }
    return render(request, 'asosiy/kirish.html', contex)

def royhat(request):
    if request.method == 'POST':
        form = RoyhatForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']

            user = User.objects.create_user(
                username=username,
                password=password,  # BU YERDA DJANGO PAROLNI O‘ZI SHIFRLAB SAQLAYDI
                first_name=first_name,
                last_name=last_name,
                parol=password
            )
            user.role = role  # Agar custom user modelda 'role' bo‘lsa
            user.save()

            return redirect('kirish')
    else:
        form = RoyhatForm()

    contex = {
        'form':form
    }

    return render(request, 'asosiy/royhat.html', contex)

def chiqish(request):
    logout(request)

    return redirect('home')
