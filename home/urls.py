from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home.html',views.home,name='home'),
    url(r'^contact.html',views.contact,name='contact'),
    url(r'^loginpage.html',views.nakalogin,name='loginpage'),
    url(r'^logoutpage.html',views.nakalogout,name='loginpage'),
    url(r'^signup.html',views.signup,name='signup'),
]
