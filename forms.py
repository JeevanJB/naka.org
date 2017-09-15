from django import forms
from membership.models import Membership
from membership.models import Volunteer

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
