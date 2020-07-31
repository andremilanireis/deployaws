from django.urls import path
from crud import views

urlpatterns = [
    path('loja/', views.loja, name='loja'),
    path('loja/instrumentos/<int:pk>/', views.instrumento_detail, name="instrumento-detail"),
    path('loja/<int:pk>/add-instrumento', views.create_instrumento, name="create-instrumento"),
    path('loja/instrumentos/<int:pk>/edit', views.edit_instrumento, name="edit-instrumento"),
    path('loja/instrumentos/<int:pk>/delete', views.delete_instrumento, name="delete-instrumento")
] 