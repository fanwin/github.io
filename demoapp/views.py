from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def csrf_get_pikachu(request):

    return render(request, 'csrf-click-get-pikachu.html')


def csrf_post_pikachu(request):
    return render(request, 'csrf-click-post-pikachu.html')


def csrf_get_dvwa_low(request):
    return render(request, 'csrf-get-dvwa-low.html')


def csrf_get_dvwa_medium(request):
    return render(request, 'csrf-dvwa-medium_192.168.43.191.html')


def csrf_post_shiyan(request):
    return render(request, 'shiyan.html')
