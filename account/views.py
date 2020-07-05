from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
import logging


logger = logging.getLogger(__name__)


def login_view(request):
    if 'username' in request.session:
        return redirect('home:home_view')
    else: 
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)
                
                logger.error(user)

                if user is not None:
                    if user.is_active:
                        #akun = Profile.objects.get(akun=user.id)
                        login(request, user)

                        #request.session['admin_id'] = akun.id
                        request.session['username'] = request.POST['username']
                        

                        return redirect('home:home_view')
                else:
                    # messages.error(request, 'username or password incorrect')
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
                    return redirect('/')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home:home_view')

    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')

