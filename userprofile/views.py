from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm
# Create your views here.

def user_login(request):
    if request.method =='POST':
        user_login_form = UserLoginForm(data=request.POST) 
        if user_login_form.is_valid():
            # clean out legal data
            data = user_login_form.cleaned_data
            # verify account and pw is correct match to a user in the db
            user = authenticate (username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse('The username or password is incorrect. Please try again.')
        else:
            return HttpResponse('The account or password is invalid.')
    elif request.method =='GET':
        user_login_form = UserLoginForm()
        context = {
            'form': user_login_form
        }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('Please use GET or POST to request data.')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('article:article_list')