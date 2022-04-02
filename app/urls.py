from django.urls import path
from .import views
urlpatterns = [
    path('',views.products, name='home'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('add-product/', views.add, name='add'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
