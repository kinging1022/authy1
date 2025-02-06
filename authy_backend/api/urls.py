from django.urls import path, include
from . import apis
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', apis.CustomTokenObtainPairView.as_view(), name='login'),
    path('signup/',apis.SignupView.as_view(), name='signup'),
    path('user/', apis.UserProfile.as_view(), name='user'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('edit/password/', apis.PasswordEdit.as_view(), name='edit_password'),
    path('request-password-reset/', apis.PasswordResetRequest.as_view(), name='request-password-reset'),
    path('reset-password/', apis.ResetPassword.as_view(), name='reset-password'),
]