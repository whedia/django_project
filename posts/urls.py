from django.urls import path
from . import views
from .views import HomePageView, CreatePostView, DeletePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), 
    path('delete/', DeletePostView.as_view(), name='delete_post'),
]