from django.shortcuts import render
from grand_ariza.models import Ariza, Natija


def arizalar(request):
    ariza_data = Ariza.objects.all()

    contex = {
        'ariza_data':ariza_data,
    }
    return render(request, 'ariza/arizalar.html', contex)

def natijalar(request):

    contex = {

    }
    return render(request, 'natija/natijalar.html', contex)
