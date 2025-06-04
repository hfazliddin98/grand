from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from user.choices import UserRoleChoice
from user.models import User
from grand_ariza.models import Ariza, Natija


# def arizalar(request):
#     ariza_data = Ariza.objects.all()

#     contex = {
#         'ariza_data':ariza_data,
#     }
#     return render(request, 'ariza/arizalar.html', contex)


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
