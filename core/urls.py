from django.urls import path
from core.views import farm_view, home_view, post_detail

app_name = 'blog'

urlpatterns = [
    path('farm/', farm_view, name='farm'),
    path('', home_view, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail')
]