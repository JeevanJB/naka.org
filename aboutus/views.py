from django.shortcuts import render

# Create your views here.

# Create your views here.
def aboutus(request):
    template = 'aboutus/aboutus.html'
    my_dict = {'insert_me' : 'Hi I am from aboutus.html'}
    return render(request,template,context=my_dict)
