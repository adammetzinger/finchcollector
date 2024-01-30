from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.finch_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('birds/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('birds/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
]