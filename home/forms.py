from django import forms
from django.contrib.auth.models import User
from home.models import Profile
from home.models import Contact
#since we dont store contact info in DB there is no model class for contact

class contactForm(forms.ModelForm): #forms.Form as there is no model required
    class Meta:
        model = Contact
        fields = '__all__'
    """
    contact_name = forms.CharField(max_length=50)
    contact_email = forms.EmailField(max_length=80)
    contact_comment = forms.CharField(required=True, widget = forms.Textarea)
    """
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')
        #username is required field

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
