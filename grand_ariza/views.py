from django.shortcuts import render
from grand_ariza.models import Ariza, Natija


def arizalar(request):

    contex = {

    }
    return render(request, 'ariza/arizalar.html', contex)

def natijalar(request):

    contex = {

    }
    return render(request, 'natija/natijalar.html', contex)
