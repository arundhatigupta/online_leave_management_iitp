from django.db import models
from django.db.models import CASCADE
import enum


class UserAccountType(enum.Enum):
    S = 'Student'
    AA = 'Authority'


class RoleType(enum.Enum):
    FAD = 'Faculty Advisor'
    GHW = 'Warden - Girls Hostel'
    BHW = 'Warden - Boys Hostel'
    SUP = 'Supervisor'
    OTH = 'Other'


class DesignationType(enum.Enum):
    ASIP = 'Assistant Professor'
    ASOP = 'Associate Professor'
    PROF = 'Professor'
    OTH = 'Other'


class ProgramType(enum.Enum):
    BTC = 'Bachelor of Technology'
    MTC = 'Master of Technology'
    MSC = 'Master of Science'
    PHD = 'Doctorate of Philosophy'
    OTH = 'Other'


class DisciplineType(enum.Enum):
    CSE = 'Computer Science and Engineering'
    EE = 'Electrical Engineering'
    CEE = 'Civil and Environmental Engineering'
    CBE = 'Chemical and Biochemical Engineering'
    ME = 'Mechanical Engineering'
    MME = 'Metallurgical and Materials Engineering'
    MSE = 'Material Science and Engineering'
    CHEM = 'Chemistry'
    MATHS = 'Mathematics'
    PHY = 'Physics'
    HSS = 'Humanities and Social Sciences'
    MNC = 'Mathematics and Computing'
    MT = 'Mechatronics'
    NT = 'Nanoscience and Technology'
    CM = 'Communication System engineering'
    OTH = 'Other'


class GenderType(enum.Enum):
    M = 'Male'
    F = 'Female'
    O = 'Other'


class HostelType(enum.Enum):
    BH = 'Boys Hostel'
    GH = 'Girls Hostel'


# models
class UserAccount(models.Model):
    user = models.OneToOneField('auth.User', related_name='user_account', on_delete=CASCADE, null=True)
    user_type = models.CharField(max_length=2,
                                 choices=[(account_type.name, account_type.value) for account_type in UserAccountType],
                                 default=UserAccountType.S.name)

    def __str__(self):
        return str(self.user.id) + " - " + self.user.first_name + " " + self.user.last_name


class Student(models.Model):
    roll_number = models.CharField(max_length=10)
    year_of_joining = models.IntegerField(default=2000)
    current_year = models.IntegerField(default=1)
    program = models.CharField(max_length=5,
                               choices=[(program_type.name, program_type.value) for program_type in ProgramType],
                               default=ProgramType.BTC.name)
    discipline = models.CharField(max_length=50,
                                  choices=[(discipline_type.name, discipline_type.value) for discipline_type in
                                           DisciplineType],
                                  default=DisciplineType.CSE.name)
    gender = models.CharField(max_length=1,
                              choices=[(gender_type.name, gender_type.value) for gender_type in GenderType],
                              default=GenderType.M.name)
    hostel = models.CharField(max_length=2,
                              choices=[(hostel_type.name, hostel_type.value) for hostel_type in HostelType],
                              default=HostelType.BH.name)
    block = models.CharField(max_length=1)
    room_number = models.IntegerField(default=0)
    user_account = models.OneToOneField(UserAccount, related_name='student', on_delete=CASCADE, null=True)

    def __str__(self):
        return str(
            self.user_account.id) + " - " + self.user_account.user.first_name + "  " + self.user_account.user.last_name


class ApprovingAuthority(models.Model):
    emp_id = models.CharField(max_length=10)
    role = models.CharField(max_length=3, choices=[(role_type.name, role_type.value) for role_type in RoleType],
                            default=RoleType.FAD.name)
    designation = models.CharField(max_length=4, choices=[(des_type.name, des_type.value)
                                                          for des_type in DesignationType],
                                   default=DesignationType.OTH.name)
    user_account = models.OneToOneField(UserAccount, related_name='authority', on_delete=CASCADE, null=True)

    def __str__(self):
        return str(
            self.user_account.id) + " - " + self.user_account.user.first_name + "  " + self.user_account.user.last_name
