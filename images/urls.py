from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_auth_view, name='home'),
    path('workspace/', views.gallery_view, name='gallery'),
    path('upload/', views.upload_image_view, name='upload_image'),
    path('delete/<int:pk>/', views.delete_image_view, name='delete_image'),
    path('logout/', views.logout_view, name='logout'),
]