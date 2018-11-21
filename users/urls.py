from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
