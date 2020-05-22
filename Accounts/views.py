from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
import bcrypt
from travello.models import passhash,contact



# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists()is False:
            messages.info(request,'Username not found.')
            return redirect('login')
        else:
            if username == 'sumos':
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect("/")
                else:
                    messages.info(request, 'Invalid Password0')
                    return redirect('login')
            else:
                pdata = passhash.objects.get(user=username)

                p1 = bcrypt.hashpw(password.encode('utf-8'), pdata.salt.encode('utf-8'))
                user = auth.authenticate(username=username, password=p1)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'Invalid Password')
                    return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #print("username taken")
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                #print('email taken')
                messages.info(request, 'email taken')
                return redirect('register')
            else:

                salt= bcrypt.gensalt()
                salt1=salt.decode('utf-8')
                hashed = bcrypt.hashpw(password1.encode('utf-8'), salt)

                user= User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,password=hashed)
                user.save();
                user_salt = passhash.objects.create(salt= salt1,user=username)
                user_salt.save();
                print("user created")

                return redirect('login')
        else:
            #print('password matched')
            messages.info(request, 'password not matched')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def contacts(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact = contact.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,subject=subject,message=message)
        Contact.save()
        return redirect('/')
    else:
        return render(request,'contact.html')





