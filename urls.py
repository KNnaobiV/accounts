from django.urls import path, include
import django.contrib.auth.urls
from accounts import views
from accounts.api.urls import urlpatterns as api_urls

app_name = 'accounts'

urlpatterns = [
    path('login/', views.DefaultLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls'),),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
]

urlpatterns += api_urls