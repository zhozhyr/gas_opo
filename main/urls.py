from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_view, name='display_data'),
    path('create_tu/', views.create_tu, name='create_tu'),
    path('delete/<int:pk>/', views.delete_view, name='delete_item'),
    path('edit/<int:pk>/', views.edit_view, name='edit_item'),
]