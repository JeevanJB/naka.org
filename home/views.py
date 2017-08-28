from django.shortcuts import render
from home.forms import contactForm, UserForm, ProfileForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import smtplib

# Create your views here.
def home(request):
    context=locals()
    template = 'home/home.html'
    my_dict = {'insert_me' : 'Hi I am from home.html'}
    return render(request,template,context)

def signUp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print('result19', profile_form.errors.as_data()) #to identify errors , 
        if user_form.is_valid() and profile_form.is_valid():
            print('Valid Form')
            user_form.save()
            profile_form.save()
            print('success', request.POST)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,'home/loginpage.html',
                            {'user_form':user_form,
                            'profile_form':profile_form})


def contact(request):
    contact_form = contactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['contact_name']
        comment = contact_form.cleaned_data['contact_comment']
        subject = 'Message from MyNaka.org site'
        contact_message = '%s %s' %(comment,name)
        #emailfrom = settings.EMAIL_HOST_USER
        emailfrom = contact_form.cleaned_data['contact_email']
        emailto = ['vaibhav@apprian.com', 'jeevan@selectiva.com']
        print(request.POST)
        send_mail(subject, contact_message, emailfrom, emailto, fail_silently=False)
        return render(request,'home/home.html')
    context = locals()
    template = 'home/contact.html'
    return render(request,template,context)
