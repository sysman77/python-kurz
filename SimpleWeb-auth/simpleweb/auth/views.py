from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from simpleweb.auth.forms import UserRegisterForm


def home_page(request):
    return render(request, "home.html")


@login_required
def profile_page(request):
    return render(request, 'profile.html')


def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'register.html',
                  {'form': UserRegisterForm()})


from django.shortcuts import render

# Create your views here.
