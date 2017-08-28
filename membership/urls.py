from django.conf.urls import url
from membership import views

urlpatterns = [
    url(r'^membership.html',views.membership,name='membership'),
]
