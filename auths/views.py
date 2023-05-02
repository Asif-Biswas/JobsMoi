from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import LoginForm, RegisterForm
from .models import Users
from django.core.mail import send_mail


# Create your views here.
def signin(request):
    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            else:
                messages.add_message(
                    request, messages.WARNING, f'You have entered incorrect credentials, please recheck.')

    form = LoginForm()

    return redirect('homePage:index')


def register(request):
    if request.method == "POST":
        print(request.POST)

        regForm = RegisterForm(request.POST)

        if regForm.is_valid():
            email = regForm.cleaned_data['email']
            if Users.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, f'Email already exists')
                return HttpResponseRedirect('/')
            password = regForm.cleaned_data['password']
            url = regForm.cleaned_data['url']
            acc_det = Users(username=email, email=email, url=url)
            acc_det.set_password(password)
            acc_det.save()

            messages.add_message(request, messages.SUCCESS, f'Your Account has been created successfully.')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, f'Please enter valid fields')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         f'You have successfully logout.')

    return HttpResponseRedirect('/')
