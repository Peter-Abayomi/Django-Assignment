from django.urls import path
from . import views

app_name = 'Blogs'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:post_id>/', views.details, name='detail'),
]
