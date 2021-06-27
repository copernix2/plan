from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.urls import reverse_lazy
#from django.contrib.auth import authenticate, login, logout
from .forms import PasswordChangingForm


class changerpassword(PasswordChangeView):
    form_class=PasswordChangingForm
    # form_class= PasswordChangeForm
    success_url= reverse_lazy('connect')
    
# Create your views here.

def indexhome(request):
    if request.method == 'POST':
        username= request.POST['email']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Bienvenue, Connection réussie')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erreur, login ou mot de passe incorrect')
            return render(request, 'index.html', {'msg': "Mot de passse ou email invalide"})
    my_user= request.user
    if my_user.is_authenticated :
        return redirect('dashboard')
    return render(request, 'index.html')

def logout_views(request):
    auth.logout(request)
    return redirect('connect')
