from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect

from .forms import UserRegisterForm,UserLoginForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def register(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance 
        form = UserRegisterForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            #password_confirm = forms.CharField(widget=forms.PasswordInput)
            email = form.cleaned_data['email']
            
            user = User.objects.create_user(username=first_name,password=password,email =email)

            # user.first_name = first_name
            # user.email = email
            # user.password = password
            user.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html', {'u_r_form': form})



def login(request):
    
    if request.method == 'POST':
        # create a form instance 
        form = UserLoginForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            nxt = request.GET.get("next", None)
            if user is not None:
                auth_login(request, user)
                
                if nxt is None:
                    return HttpResponseRedirect(reverse('store-home'))
                    #return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    return redirect(nxt)
                    
            else:
                messages.error(request,'Incorrect Password or Username')
                if nxt is None:
                    return HttpResponseRedirect(reverse('store-home'))
                else:
                    return redirect(nxt)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserLoginForm()
    return render(request,'users/login.html', {'u_l_form': form})


    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    