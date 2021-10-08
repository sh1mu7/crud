from django.urls import path
from base import views

app_name = 'base'
urlpatterns = [
    path('', views.add_show, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:id>/', views.update, name='update')

]
