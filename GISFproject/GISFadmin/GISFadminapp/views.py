from conda._vendor.auxlib.crypt import encrypt, decrypt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import NewUserForm
from .models import NewUser


# Create your views here.
def NewUserCreate(request):
    password = request.POST.get('pwd')
    username = request.POST.get('uid')
    if request.method == "POST":
        encr = encrypt(password, username)

        NewUser.objects.create(username=username, password=encr)
        # dec = decrypt(encr, username)

    return render(request, 'GISFadmin/NewUser.html')


def userregister(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(username)
            login(request, user)
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="GISFadmin/NewUserReg.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request=request, template_name="GISFadmin/NewUserReg.html", context={"form": form})


def loginView(request):
    if request.method == 'GET':
        return render(request, 'GISFadmin/login.html', {})
    else:
        username = request.POST['username']
        print('username', username)
        password = request.POST['password']
        print('password', password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('mainmenu/')
            return render(request, 'GISFadmin/mainmenu.html', {})
        else:
            return render(request, 'GISFadmin/login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'GISFadmin/logout.html', {})


def homepage(request):
    return render(request, 'GISFadmin/home.html', {})

def about(request):
    return render(request,'GISFadmin/About.html')

def mainmenu(request):
    return render(request, 'GISFadmin/mainmenu.html', {})

