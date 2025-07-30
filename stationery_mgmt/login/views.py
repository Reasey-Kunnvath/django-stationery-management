from django.shortcuts import render, redirect
from . import models
from login.common import common
import sweetify

# Create your views here.
def login_page(request):
    return render(request, 'login/login_page.html', {'error': request.GET.get('error', 'False'), 'message': request.GET.get('message', '')})

def auth_adm_login(request):
    if request.method == 'POST':
        if common.auth(request.POST['username'], request.POST['password']):
            return render(request, 'test_page/test_page.html', {'message': 'Login successful'})
        else:
            sweetify.error(request, 'Login Failed', text='Invalid username or password', persistent='OK')
            return redirect('login_page')

def home_page(request):
    return render(request, 'test_page/test_page.html')