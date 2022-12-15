from django.urls import path 
from .views import CreateAccountView, UserProfileView, AuthorView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/', UserProfileView.as_view(), name='myprofile'),
    path('profile/<int:pk>/', AuthorView.as_view(), name='profile'),
]