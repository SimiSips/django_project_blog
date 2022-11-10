from django.urls import path, include
from core.views import deletePost, EditPostView, PostListView, AddPostView,farm_view, register_request, logout_request, login_request, home_view, post_detail, profile_view, mypost_view, UserEditView
from . import views
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
    path('<pk>/update', UserEditView.as_view(), name="edit_profile"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('myposts', PostListView.as_view(), name='myposts'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('update_post/<int:pk>/', EditPostView.as_view(), name='update_post'),
    path('<id>/delete', deletePost, name="delete_post")

]