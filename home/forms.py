from django import forms
from django.contrib.auth.models import User
from home.models import Profile

#since we dont store contact info in DB there is no model class for contact
class contactForm(forms.Form):
    contact_name = forms.CharField(max_length=50)
    contact_email = forms.EmailField(max_length=80)
    contact_comment = forms.CharField(required=True, widget = forms.Textarea)

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','username','password')
        #username and email are same<assumption>. username is required field

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
