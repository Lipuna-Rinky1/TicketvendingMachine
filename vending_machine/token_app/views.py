from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TokenGenerationForm
from .models import  Department, Doctor, Token, User

from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required


def token_generate_view(request):

    form = TokenGenerationForm()
    if request.method == 'POST':
        form = TokenGenerationForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data
            doct = str(data["doctor"]).split(" ")
            dept = str(data["department"])
            token_list = Token.objects.all()
            index = 1
            form.instance.token = dept[0] + "-" +  doct[0][0] + doct[-1][0] + "-" + str(len(token_list) + 1)
            form.save()
            return redirect('list')
    return render(request, 'token/token.html', {'form': form})

# AJAX
def load_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id).all()
    return render(request, 'token/doctor_dropdown_list_options.html', {'doctors': doctors})

@login_required
def delete(request):
    cat = Token.objects.all()
    cat.delete()
    return redirect('generate_token')  

def token_list(request):
    token_list = Token.objects.all()
    tokens = {'token_list':token_list}
    return render(request, 'token/token_list.html', context=tokens)


def registration(request):
    return render(request, 'token/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Incorrect Username or password')
            return redirect('login')
    else:
        return render(request, 'token/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def instertData(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email'] 
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username allready exists...')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email allready exists...')
                return redirect('registration')
            else:
                insrt = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password2)
                insrt.save()
                messages.success(request, 'User Submit successfully...!')
                return redirect('generate_token')
        else:            
            messages.error(request, 'Password does not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')

