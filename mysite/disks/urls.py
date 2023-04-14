from django.urls import path

from . import views

app_name = 'disks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='album_detail'),

]
