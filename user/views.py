from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.choices import UserRoleChoice
from user.forms import KirishForm, AdminQoshishForm
from user.serializers import UserGetSerializer, UserPostSerializer




@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        if request.user.role == UserRoleChoice.SUPERADMIN:
            return render(request, 'superadmin/home.html')
        elif request.user.role == UserRoleChoice.ADMIN:
            return render(request, 'admin/home.html')
        elif request.user.role == UserRoleChoice.TALABA:
            return render(request, 'talaba/home.html')
    else:

        return redirect('kirish')

@csrf_exempt
def admin_kirish(request):
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

@csrf_exempt
def kirish(request):
    import pandas as pd
    import requests
    def talaba_user_token(username, password):

        login_endpoint = "https://student.kokandsu.uz/rest/v1/auth/login"

        payload = {
        "login": '356241101810',
        "password": "Marjona2006"
        }
        req = requests.post(login_endpoint, data=payload)
        data = req.json()
        user_token = data["data"]["token"]

        return user_token
    
    def talaba_malumot(username, password):
        user_token = talaba_user_token(username, password)
        retrieve_user_info_endpoint = "https://student.kokandsu.uz/rest/v1/account/me"
        headers = {
            "Authorization": f"Bearer {user_token}"
        }
        req = requests.get(retrieve_user_info_endpoint, headers=headers)
        df = req.json()['data']
        return df
    
    def talaba_gpa(username, password):
        user_token = talaba_user_token(username, password)
        retrieve_user_info_endpoint = "https://student.kokandsu.uz/rest/v1/data/student-gpa-list"
        headers = {
            "Authorization": f"Bearer {user_token}"
        }
        req = requests.get(retrieve_user_info_endpoint, headers=headers)
        df = req.json()['data']
        if df:
            qiymat = df
        else:
            qiymat = 0
        return qiymat
    
    def talaba_create(username, password):
        talaba  = talaba_malumot(username, password)
        gpa  = talaba_gpa(username, password)

        if User.objects.filter(username=username):
            User.objects.filter(username=username).update(
                last_name=talaba['second_name'],
                first_name=talaba['first_name'],
                sharif=talaba['third_name'],
                fakultet=talaba['faculty']['name'],
                yonalish=talaba['specialty']['name'],
                kurs=talaba['level']['name'],
                guruh=talaba['group']['name'],
                gpa=gpa,
                password=make_password(password),
                parol = password
            )
            print('talaba yangilandi')
        else:
            User.objects.create(
                username=username,
                last_name=talaba['second_name'],
                first_name=talaba['first_name'],
                sharif=talaba['third_name'],
                fakultet=talaba['faculty']['name'],
                yonalish=talaba['specialty']['name'],
                kurs=talaba['level']['name'],
                guruh=talaba['group']['name'],
                gpa=gpa,
                password=make_password(password),
                parol = password
            )
            print('talaba yangi yaratildi')
        talaba1 = talaba['full_name']
        return talaba1

    if request.method == 'POST':
        form = KirishForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            talaba = talaba_create(username, password)
            print(talaba)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # yoki istalgan sahifaga yo‘naltirish
            else:
                form.add_error(None, 'Login yoki parol noto‘g‘ri')
    else:
        form = KirishForm()

    contex = {
        'form':form,
    }
    return render(request, 'asosiy/kirish.html', contex)

@csrf_exempt
def admin_qoshish(request):
    if request.method == 'POST':
        form = AdminQoshishForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']
            bolim = form.cleaned_data['bolim']

            user = User.objects.create_user(
                username=username,
                password=password,  # BU YERDA DJANGO PAROLNI O‘ZI SHIFRLAB SAQLAYDI
                first_name=first_name,
                last_name=last_name,
                parol=password
            )
            user.role = role  # Agar custom user modelda 'role' bo‘lsa
            user.bolim = bolim  # Agar custom user modelda 'bolim' bo‘lsa
            user.save()

            return redirect('kirish')
    else:
        form = AdminQoshishForm()

    contex = {
        'form':form
    }

    return render(request, 'superadmin/admin_qoshish.html', contex)


@csrf_exempt
def chiqish(request):
    logout(request)

    return redirect('home')



@csrf_exempt
def adminlar(request):
    adminlar = User.objects.filter(role=UserRoleChoice.ADMIN)
    contex = {
        'adminlar':adminlar,
    }
    return render(request, 'superadmin/adminlar.html', contex)

@csrf_exempt
def malumotlarim(request):
    last_name = request.user.last_name
    first_name = request.user.first_name
    sharif = request.user.sharif
    fakultet = request.user.fakultet
    yonalish = request.user.yonalish
    kurs = request.user.kurs
    guruh = request.user.guruh
    gpa = request.user.gpa
    contex = {
        'last_name':last_name,
        'first_name':first_name,
        'sharif':sharif,
        'fakultet':fakultet,
        'yonalish':yonalish,
        'kurs':kurs,
        'guruh':guruh,
        'gpa':gpa,
    }
    return render(request, 'talaba/malumotlarim.html', contex)


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'role']
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return UserGetSerializer
        return UserPostSerializer  # POST, PUT, PATCH uchun
