from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
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


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'role']
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return UserGetSerializer
        return UserPostSerializer  # POST, PUT, PATCH uchun
