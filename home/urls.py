from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home.html',views.home,name='home'),
    url(r'^contact.html',views.contact,name='contact'),
    url(r'^loginpage.html',views.login,name='loginpage'),
    url(r'^signup.html',views.signup,name='signup'),
]
