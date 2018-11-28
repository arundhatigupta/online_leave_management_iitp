from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.forms import SignUpForm
from users.models import ApprovingAuthority, Student, UserAccount


def signup(request):
    if request.method == "POST":
        print(request.POST)
        password = request.POST.get('password', '')
        re_enter_password = request.POST.get('re_enter_password', '')
        user_type = request.POST.get('user_type', '')

        if password == re_enter_password:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user = User.objects.create_user(username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user_account = UserAccount.objects.create(
                user=user,
                user_type=user_type
            )
            user_account.save()
            if user_type == 'S':
                print(request.POST)
                roll_number = request.POST.get('roll_number')
                student = Student.objects.create(user_account=user_account, roll_number=roll_number)
                student.save()
            else:
                emp_id = request.POST.get('emp_id')
                authority = ApprovingAuthority.objects.create(user_account=user_account, emp_id=emp_id)
                authority.save()
            authenticate(username=username, password=password)
            return redirect('users:login')
        else:
            return redirect('users:signup')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
