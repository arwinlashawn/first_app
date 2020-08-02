from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', views.create, name='notes-home'),
    #path('', PostListView.as_view(), name='notes-home'),
    path('create/', views.create, name='notes-create'),
    path('about/', views.about, name='notes-about'),
]


# looking for notes/post_list.html
# app/model_viewtype.html
