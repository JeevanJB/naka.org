from django.shortcuts import render
from membership.forms import MembershipForm

# Create your views here.
def membership(request):
    if request.method == 'POST':
        membership_form = MembershipForm(request.POST)
        print('result25', membership_form.errors.as_data()) #to identify errors
        if membership_form.is_valid():
            print('Valid Form')
            profile = membership_form.save(commit=False)
            profile.save()
            print('success', request.POST)
    else:
        membership_form = MembershipForm()
    return render(request,'membership/membership.html',
                            {'membership_form':membership_form})
