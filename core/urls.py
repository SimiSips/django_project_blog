from django.urls import path, include
from core.views import farm_view, register_request, logout_request, login_request, home_view, post_detail, profile_view, mypost_view

app_name = 'blog'

urlpatterns = [
    path('farm/', farm_view, name='farm'),
    path('', home_view, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    # path('accounts/profile', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('myposts', mypost_view, name='myposts'),
]