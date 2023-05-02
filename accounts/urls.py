from django.urls import path
from django.contrib.auth import views as auth_views
from my_site import settings
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html', next_page=settings.LOGIN_REDIRECT_URL), name='logout'),
    path('signup/', views.InvestorFormView.as_view(), name='signup'),  
]