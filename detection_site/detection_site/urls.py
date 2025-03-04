"""detection_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add_image/', views.add_image_feed, name='add_image_feed'),
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register, name='register'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('add_image/', views.add_image_feed, name='add_image_feed'),
# ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('object_detection.urls')),  # Подключаем маршруты приложения
# ]


from django.contrib import admin
from django.urls import include, path
from . import views  # Импортируем views

urlpatterns = [
    path('admin/', admin.site.urls),  # Если ты хочешь добавить админку
    path('', views.home, name='home'),
    path('add_image/', views.add_image_feed, name='add_image_feed'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('', include('object_detection.urls')),  # Подключаем маршруты приложения
]
