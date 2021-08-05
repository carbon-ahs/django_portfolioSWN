from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all-comments/', views.all_commentsFV, name='all-comments'),
]