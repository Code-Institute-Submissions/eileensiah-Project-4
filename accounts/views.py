from django.urls import reverse_lazy, resolve, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserLoginForm
from accounts.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')

"""
This is login function
"""
def login(request):
    if request.method == "POST":
        # populate the login form with the user's input
        login_form = UserLoginForm(request.POST)
        
        # if the input to the login form is valid
        if login_form.is_valid():
            # use auth.authenticate to check if the
            # user name and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            #if there is a user (meaning, user is not None)
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {
            'form':form
        })
        
        
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # check if the username and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                # actually log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successful")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('index'))
        else:
            return render(request, "signup.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "signup.html", {
            'form': register_form
        })
    

    
def account_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('account', username=user.username)
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'account_edit.html', {'form': form})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account', username=user.username)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })