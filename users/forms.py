from django import forms
from users.models import UserAccountType


class SignUpForm(forms.Form):
    user_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(user_account_type.name, user_account_type.value) for user_account_type in
                 UserAccountType]
    )
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    roll_number = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Roll no'}))
    emp_id = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Employee Id'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    re_enter_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
