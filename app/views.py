from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from app.forms import *
from app.models import Leave, LeaveApprovingWarden, LeaveApprovingFaculty


def index(request):
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    return redirect('users:login')


def profile(request):
    user = request.user
    try:
        user_account = request.user.user_account

        if user_account.user_type == 'S':
            student = user_account.student
            context = {'student': student}

            if request.method == 'POST':
                user.first_name = request.POST.get('first_name', '')
                user.last_name = request.POST.get('last_name', '')
                user.save()

                student.current_year = request.POST.get('current_year', '')
                student.program = request.POST.get('program', '')
                student.discipline = request.POST.get('discipline', '')
                student.block = request.POST.get('block', '')
                student.room_number = request.POST.get('room_number', '')
                student.save()
            return render(request, 'app/student_profile.html', context)

        elif user_account.user_type == 'AA':
            authority = user_account.authority
            context = {'authority': authority}

            if request.method == 'POST':
                user.first_name = request.POST.get('first_name', '')
                user.last_name = request.POST.get('last_name', '')
                user.save()

                # authority.designation = request.POST.get('designation', '')
                # authority.role = request.POST.get('role', '')
                # authority.save()

            return render(request, 'app/approving_authority_profile.html', context)
    except:
        return redirect(request, 'app/error.html', {})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {
        'form': form
    })


def dashboard(request):
    user_account = request.user.user_account
    if user_account.user_type == 'S':
        return render(request, 'app/student_dashboard.html', {})
    else:
        return render(request, 'app/authority_dashboard.html', {})


def leave_create(request):
    student = request.user.user_account.student
    if request.method == "POST":
        leave = Leave.objects.create(
            reason_for_leave=request.POST.get('reason_for_leave', ''),
            going_to_place=request.POST.get('going_to_place', ''),
            going_to_type=request.POST.get('going_to_type', ''),
            date_of_leaving=request.POST.get('date_of_leaving', ''),
            date_of_returning=request.POST.get('date_of_returning', ''),
        )
        leave.student = request.user.user_account.student
        leave.faculty = \
        LeaveApprovingFaculty.objects.filter(batch=student.year_of_joining).filter(program=student.program).filter(
            discipline=student.discipline)[0]
        leave.warden = LeaveApprovingWarden.objects.filter(hostel=student.hostel)[0]
        leave.save()
        return redirect('app:leave_detail', pk=leave.pk)
    else:
        form = LeaveForm()
    return render(request, 'app/leave_create.html', {'form': form})


def leave_detail(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    return render(request, 'app/leave_detail.html', {'leave': leave})


def leave_edit(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == "POST":
        leave.reason_for_leave = request.POST.get('reason_for_leave', '')
        leave.going_to_place = request.POST.get('going_to_place', '')
        leave.going_to_type = request.POST.get('going_to_type', '')
        leave.date_of_leaving = request.POST.get('date_of_leaving', '')
        leave.date_of_returning = request.POST.get('date_of_returning', '')
        if request.user.user_account.user_type == 'S':
            leave.student = request.user.user_account.student
        else:
            leave.leave_status = request.POST.get('leave_status', 'PEN')
        leave.save()
        return redirect('app:leave_detail', pk=leave.pk)
    else:
        user_account = request.user.user_account
        if user_account.user_type == 'AA':
            if user_account.authority.role == 'FAD':
                form = LeaveForm(leave.__dict__, can_approve=True)
            else:
                form = LeaveForm(leave.__dict__, can_approve=True, is_warden=True)
        else:
            form = LeaveForm(leave.__dict__, can_approve=False)
    return render(request, 'app/leave_edit.html', {'form': form})


def leaves_pending(request):
    user_account = request.user.user_account
    if user_account.user_type == 'S':
        leaves = Leave.objects.filter(student=user_account.student).exclude(leave_status="APPW")
        return render(request, 'app/leaves_list.html', {'leaves': leaves, 'can_edit': True})
    else:
        authority_type = user_account.authority.role
        if authority_type == 'FAD':
            leaves = Leave.objects.filter(faculty=user_account.authority.faculty).filter(leave_status="PEN")
        else:
            leaves = Leave.objects.filter(warden=user_account.authority.warden).filter(leave_status="APPF")
        return render(request, 'app/leaves_list.html', {'leaves': leaves, 'can_edit': True})


def leaves_past(request):
    user_account = request.user.user_account
    if user_account.user_type == 'S':
        leaves = Leave.objects.filter(student=user_account.student).filter(leave_status="APPW")
        return render(request, 'app/leaves_list.html', {'leaves': leaves, 'can_edit': False})
    else:
        authority_type = user_account.authority.role
        if authority_type == 'FAD':
            leaves = Leave.objects.filter(faculty=user_account.authority.faculty).exclude(leave_status="PEN")
        else:
            leaves = Leave.objects.filter(warden=user_account.authority.warden).exclude(
                leave_status="PEN").exclude(leave_status="APPF")
        return render(request, 'app/leaves_list.html', {'leaves': leaves, 'can_edit': False})
