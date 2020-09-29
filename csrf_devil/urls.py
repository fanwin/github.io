"""csrf_devil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from demoapp.views import csrf_get_pikachu, csrf_post_pikachu, csrf_get_dvwa_low, csrf_get_dvwa_medium, csrf_post_shiyan

urlpatterns = [
    url('admin/', admin.site.urls),
    url('csrf_get_pikachu/', csrf_get_pikachu),
    url('csrf_post_pikachu/', csrf_post_pikachu),
    url('csrf_get_dvwa_low/', csrf_get_dvwa_low),
    url('192.168.43.191/', csrf_get_dvwa_medium),   # TODO
    url('shiyan/', csrf_post_shiyan),
]
