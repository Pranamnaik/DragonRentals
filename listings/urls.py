from django.urls import path, include

from . import views

urlpatterns = [
    path('search/', views.home, name='property_search'),  # New search URL

    path('create/', views.create_property, name='create_property'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
    path('<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('<int:pk>/delete/', views.delete_property, name='delete_property'),
]
