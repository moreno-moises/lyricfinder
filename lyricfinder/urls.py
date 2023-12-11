"""
URL configuration for lyricfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from dashboard import views
from django.urls import path, include
from dashboard.views import home, search_song, signup, profile, bookmark_song, custom_logout


urlpatterns = [
    path('', home, name='home'),
    path('search/', views.search_song, name='search_song'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile'),   
    path('search_results/<int:song_id>/', views.search_results, name='search_results'),
    path('bookmark_song/', bookmark_song, name='bookmark_song'),
    path('logout/', custom_logout, name='logout'),
]