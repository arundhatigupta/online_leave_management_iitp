from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from online_leave_management_iitp import settings
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change-password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leave/<int:pk>/', views.leave_detail, name='leave_detail'),
    path('leave/apply/', views.leave_create, name='leave-apply'),
    path('leaves/pending/', views.leaves_pending, name='leaves-pending'),
    path('leaves/past/', views.leaves_past, name='leaves-past'),
    path('leave/<int:pk>/edit/', views.leave_edit, name='leave_edit'),
]
if not settings.DEBUG:
    urlpatterns += path('', (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                 {'document_root': settings.STATIC_ROOT}), )
