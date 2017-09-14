"""naka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views
from aboutus import views
from membership import views

#Any Extension can be used in-place of 'naka' & will be reflected in Browser URL
urlpatterns = [
    url(r'^naka/',include('home.urls')),
    url(r'^naka/',include('aboutus.urls')),
    url(r'^naka/',include('membership.urls')),
    url(r'^admin/', admin.site.urls),
]
