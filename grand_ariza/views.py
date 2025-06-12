from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user.choices import UserRoleChoice
from grand_ariza.choices import ArizaRoleChoice
from user.models import User
from grand_ariza.models import Ariza, Natija



@login_required
def talaba_ariza_create(request):
    try:
        ariza = Ariza.objects.get(user=request.user)
        return HttpResponse("Sizning arizangiz allaqachon mavjud")
    except Ariza.DoesNotExist:
        print('Ariza yangi yaratish')
        Ariza.objects.create(
            user=request.user,  # Faqat .id emas, butun obyekt
            ariza_role=ArizaRoleChoice.OQUV
        )
        return HttpResponse('Ariza yaratildi !!!')

@csrf_exempt
def arizalar(request):
    if request.user.is_authenticated:
        if request.user.role == UserRoleChoice.SUPERADMIN:
            ariza_data = Ariza.objects.all()

            contex = {
                'ariza_data':ariza_data,
            }
            return render(request, 'superadmin/arizalar.html', contex)
        elif request.user.role == UserRoleChoice.ADMIN:
            ariza_data = Ariza.objects.all()

            contex = {
                'ariza_data':ariza_data,
            }
            return render(request, 'admin/arizalar.html', contex)
        elif request.user.role == UserRoleChoice.TALABA:
            user_data = User.objects.filter(id=request.user.id)
            ariza_data = Ariza.objects.filter(user=request.user.id)

            contex = {
                'ariza_data':ariza_data,
                'user_data':user_data,
            }
            return render(request, 'talaba/arizalar.html', contex)
    else:

        return redirect('kirish')
    
def natijalar(request):
    if request.user.is_authenticated:
        if request.user.role == UserRoleChoice.SUPERADMIN:
            natija_data = Natija.objects.all()

            contex = {
                'natija_data':natija_data,
            }
            return render(request, 'superadmin/natijalar.html', contex)
        elif request.user.role == UserRoleChoice.ADMIN:
            natija_data = Natija.objects.all()

            contex = {
                'natija_data':natija_data,
            }
            return render(request, 'admin/natijalar.html', contex)
        elif request.user.role == UserRoleChoice.TALABA:
            natija_data = Natija.objects.all()

            contex = {
                'natija_data':natija_data,
            }
            return render(request, 'talaba/natijalar.html', contex)
    else:

        return redirect('kirish')
