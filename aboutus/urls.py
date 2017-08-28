from django.conf.urls import url
from aboutus import views

urlpatterns = [
    url(r'^aboutus.html',views.aboutus,name='aboutus'),
]
