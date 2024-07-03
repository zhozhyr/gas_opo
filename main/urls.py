from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_view, name='display_data'),
    path('export/', views.export_to_excel, name='export_to_excel'),
]