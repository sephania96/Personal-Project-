from django.urls import path, include
from users.views import dashboard
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('accounts/logout/', auth_views.LogoutView.as_view(next_page="dashboard.html"), name='logout'),
    # path("", TemplateView.as_view(template_name="logged_out.html"), name="dashboard"),
]