from django.urls import reverse_lazy, resolve, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserLoginForm, AgencySignUpForm, EmployerSignUpForm
from accounts.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AgencySignUpView(CreateView):
    model = User
    form_class = AgencySignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['choices'] = 'Agency'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('enquiry')
        
class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['choices'] = 'Employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    
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
    
