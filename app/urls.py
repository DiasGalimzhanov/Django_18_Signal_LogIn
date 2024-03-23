from django.urls import path
from .views import home, SignUpView, CustomLoginView, profile

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
]
