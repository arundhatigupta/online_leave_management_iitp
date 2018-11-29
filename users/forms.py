from django import forms
from users.models import UserAccountType, ProgramType, DisciplineType, GenderType, HostelType


class SignUpForm(forms.Form):
    user_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(user_account_type.name, user_account_type.value) for user_account_type in
                 UserAccountType]
    )
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    roll_number = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Roll no'}))
    year_of_joining = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Year of Joining'}))
    program_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(program_type.name, program_type.value) for program_type in
                 ProgramType]
    )
    discipline_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(discipline_type.name, discipline_type.value) for discipline_type in
                 DisciplineType]
    )
    gender_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(gender_type.name, gender_type.value) for gender_type in
                 GenderType]
    )
    hostel_type = forms.MultipleChoiceField(
        label=False,
        widget=forms.Select,
        choices=[(hostel_type.name, hostel_type.value) for hostel_type in
                 HostelType]
    )
    emp_id = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Employee Id'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    re_enter_password = forms.CharField(label=False,
                                        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
