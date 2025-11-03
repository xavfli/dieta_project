from django.contrib import admin
from django.urls import path
from app_dieta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('api/submit/', views.submit_user, name='submit_user'),
]
