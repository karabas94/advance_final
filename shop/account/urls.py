from django.urls import path
from account.views import RegisterFormView, login_request, logout_request, UpdateProfile, UserProfile, PublicProfile


app_name = 'account'
urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),

    path('login/', login_request, name='login'),
    path('update_profile/', UpdateProfile.as_view(), name='update_profile'),

    path('', UserProfile.as_view(), name='profile'),
    path('<int:pk>/', PublicProfile.as_view(), name='user_profile'),

    path('logout', logout_request, name="logout"),
]
