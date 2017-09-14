from django.shortcuts import render
from home.forms import UserForm, ProfileForm, contactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import smtplib
from simple_salesforce import Salesforce


# Create your views here.
def home(request):
    context=locals()
    template = 'home/home.html'
    return render(request,template,context)

def nakalogin(request):
    print('17')
    context=locals()
    if request.method == 'POST':
        uname = request.POST.get('txtusername', '')
        passw = request.POST.get('txtpassword', '')
        user = authenticate(username = uname, password = passw)
        print('18 = ', uname, passw, '19 = ', user)
        if user is not None and user.is_active:
            login(request, user)
            return render(request,'home/home.html',context)
        else:
            return render(request,'home/loginpage.html',context)
    template = 'home/loginpage.html'
    return render(request,template,context)

@login_required
def nakalogout(request):
    logout(request)
    return render(request,'home/home.html')

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print('40 = ', profile_form.errors.as_data())
        print('41 = ', user_form.errors.as_data())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('test')
            return render(request,'home/home.html')
    else:
        user_form = UserForm()
        profile_form = ProfileForm
    context = {'user_form':user_form,
                'profile_form':profile_form}
    template = 'home/signup.html'
    return render(request,template,context)

def contact(request):
    contact_form = contactForm(request.POST or None)
    if contact_form.is_valid():
        print('63 = ', request.POST)
        contact_form.save()
        name = contact_form.cleaned_data['fullname']
        email = contact_form.cleaned_data['email']
        sf = Salesforce(instance_url='https://login.salesforce.com', session_id='')
        sf1 = Salesforce(username='bodasjeevan@gmail.com', password='asdf@1234', security_token='USkWqAEFCNHiMZarRL8V6kKc')
        sf3 = sf1.Contact.create({'LastName':name,'Email':email})
        print('sf3 = ', sf3)
        return render(request,'home/home.html')
        """
        name = contact_form.cleaned_data['contact_name']
        comment = contact_form.cleaned_data['contact_comment']
        subject = 'Message from MyNaka.org site'
        contact_message = '%s %s' %(comment,name)
        #emailfrom = settings.EMAIL_HOST_USER
        emailfrom = contact_form.cleaned_data['contact_email']
        emailto = ['vaibhav@apprian.com', 'jeevan@selectiva.com']
        print(request.POST)
        #send_mail(subject, contact_message, emailfrom, emailto, fail_silently=False)
        return render(request,'home/home.html')
        """
    context = {'contact_form':contact_form}
    template = 'home/contact.html'
    return render(request,template,context)
