from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('panfilov/', views.panfilov_static_page, name='panfilov_static_page'),
    path('momyshuly/', views.momyshuly_static_page, name='momyshuly_static_page'),
    path('panfilovcy/', views.panfilovcy_static_page, name='panfilovcy_static_page'),
    path('school_info/', views.school_info, name='school_info'),
    path('panfilov_school_info/', views.panfilov_school_info, name='panfilov_school_info'),
]
