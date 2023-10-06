from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # view to show and individual data from DB
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # view to show all the data from DB
    path('', PostList.as_view(), name='listcreate')
]