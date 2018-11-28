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