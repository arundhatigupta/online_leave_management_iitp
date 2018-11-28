from django import forms
from django.db import models
from django.db.models import CASCADE
from users.models import ProgramType, DisciplineType, HostelType
import enum

# model for leave
from django.urls import reverse


class PlaceType(enum.Enum):
    NAT = 'Native'
    OTH = 'Other'


class LeaveStatusType(enum.Enum):
    PEN = 'Pending'
    APPF = 'Approved by Faculty'
    APPW = 'Approved by Warden'
    REJ = "Rejected"


class Leave(models.Model):
    # leave_id = models.CharField(max_length=12)
    student = models.ForeignKey('users.Student', on_delete=CASCADE, null=True)
    faculty = models.ForeignKey('app.LeaveApprovingFaculty', on_delete=CASCADE, null=True)
    warden = models.ForeignKey('app.LeaveApprovingWarden', on_delete=CASCADE, null=True)
    leave_status = models.CharField(max_length=10,
                                    choices=[(status_type.name, status_type.value) for status_type in
                                             LeaveStatusType],
                                    default=LeaveStatusType.PEN.name)
    reason_for_leave = models.CharField(max_length=200)
    going_to_type = models.CharField(max_length=3,
                                     choices=[(place_type.name, place_type.value) for place_type in
                                              PlaceType],
                                     default=PlaceType.NAT.name)
    going_to_place = models.CharField(max_length=50)
    date_of_leaving = models.DateTimeField(null=True)
    date_of_returning = models.DateTimeField(null=True)

    # TODO: Add support for uploading supporting docs
    # supporting_documents = models.FileField()


class LeaveApprovingFaculty(models.Model):
    batch = models.IntegerField()
    program = models.CharField(max_length=5,
                               choices=[(program_type.name, program_type.value) for program_type in ProgramType],
                               default=ProgramType.BTC.name)
    discipline = models.CharField(max_length=50,
                                  choices=[(discipline_type.name, discipline_type.value) for discipline_type in
                                           DisciplineType],
                                  default=DisciplineType.CSE.name)
    authority = models.OneToOneField('users.ApprovingAuthority', related_name='faculty', on_delete=CASCADE, null=True)


class LeaveApprovingWarden(models.Model):
    batch = models.IntegerField()
    hostel = models.CharField(max_length=2,
                              choices=[(hostel_type.name, hostel_type.value) for hostel_type in HostelType],
                              default=HostelType.BH.name)
    authority = models.OneToOneField('users.ApprovingAuthority', related_name='warden', on_delete=CASCADE, null=True)
