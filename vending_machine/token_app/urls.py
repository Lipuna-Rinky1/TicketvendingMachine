from django.urls import path
from . import views

urlpatterns = [
    path('', views.token_generate_view, name='generate_token'),
    path('ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'), # AJAX
    path('delete/', views.delete, name='delete'),
    path('list/', views.token_list, name='list'),

    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('instertData/', views.instertData, name="instertData"),
]