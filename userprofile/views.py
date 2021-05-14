from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
# decorator to verify login
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # set Pw
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # login immediately after saving the data ad return to the blog list 
            login(request, new_user)
            return redirect('article:article_list')
        else:
            return HttpResponse('Registration inputs are invalid. Please Re-enter')
    elif request.method =='GET':
        user_register_form = UserRegisterForm()
        context = {
            'form' : user_register_form
            }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse('Please use Get or Post request for Data.')

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


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        # verify logged in user
        if request.User == user:
            logout(request)
            user.delete()
            return redirect('article:article_list')
        else:
            return HttpResponse('You do not have permission to delete User')
    else:
        return HttpResponse('Submit a POST request.')