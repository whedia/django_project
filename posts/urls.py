from django.urls import path
from . import views
from .views import HomePageView, CreatePostView # new

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), # new
    path('delete/<int:pk>/', views.delete, name='delete'),
]