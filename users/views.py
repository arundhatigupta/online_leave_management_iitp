from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.forms import SignUpForm


def signup(request):
    if request.method == "POST":
        password = request.POST.get('password', '')
        re_enter_password = request.POST.get('re_enter_password', '')
        if password == re_enter_password:
            user = User.objects.create(
                username=request.POST.get('username', ''),
                first_name=request.POST.get('first_name', ''),
                last_name=request.POST.get('last_name', ''),
                password=request.POST.get('password', '')
            )
            user.save()
            return redirect('users:login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
