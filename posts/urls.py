from django.urls import path
from . import views
from .views import HomePageView, CreatePostView, DeletePostView, EditPostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), 
    path('<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'), #<int:pk> permet de désigner l'id du post a supprimer
    path('<int:pk>/edit/', EditPostView.as_view(), name='edit_post'), #<int:pk> permet de désigner l'id du post a éditer
]