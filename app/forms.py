from django import forms
from django.contrib.admin import widgets
from app.models import PlaceType, LeaveStatusType
from users.models import UserAccountType


class LeaveForm(forms.Form):
    reason_for_leave = forms.CharField()
    going_to_place = forms.CharField()
    going_to_type = forms.MultipleChoiceField(
        widget=forms.Select,
        choices=[(place_type.name, place_type.value) for place_type in
                 PlaceType]
    )
    leave_status = forms.MultipleChoiceField(
        widget=forms.Select
    )
    date_of_leaving = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
    date_of_returning = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        can_approve = kwargs.pop('can_approve', False)
        is_warden = kwargs.pop('is_warden', False)
        super(LeaveForm, self).__init__(*args, **kwargs)
        if not can_approve:
            self.fields['leave_status'].widget = forms.HiddenInput()
        choices = []
        if not is_warden:
            for status_type in LeaveStatusType:
                if status_type.name != 'APPW':
                    choices.append((status_type.name, status_type.value))
        else:
            for status_type in LeaveStatusType:
                choices.append((status_type.name, status_type.value))
        self.fields['leave_status'].choices = choices


class SignUpForm(forms.Form):
    user_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(user_account_type.name, user_account_type.value) for user_account_type in
                 UserAccountType]
    )
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    re_enter_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
