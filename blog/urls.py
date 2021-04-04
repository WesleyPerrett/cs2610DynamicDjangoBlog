from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tips/', views.tips, name='tips'),
    path('archive/', views.archive, name='archive'),
    path('<int:blog_id>/entry/', views.entry, name='entry'),
    path('<int:blog_id>/addcomment/', views.addcomment, name='addcomment'),
]