# adding this new file in Blog app as it was not there
from django.urls import path
# will import blog app views
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
    # when anyone comes to urls.py ,will check if main url PATH is int or str after blog, forwaaard to this detail
    path('<int:blog_id>/',views.detail, name='detail'),
]
