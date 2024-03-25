"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users.views import *
from .views import *
from .settings import *
from django.conf import settings
from django.conf.urls.static import static
from contact.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', ContactMessage,basename="api3")
urlpatterns = [
    path ('grappelli/',include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', test_connection),
    path('auth/', include('users.urls')),
    path('appointments/', include('appointments.urls')),
    path('schedules/', include('appointments.urls')),
    path('ratings/', include('ratings.urls')),  
    path('doctors/', include('doctors.urls')),
    path('offers/', include('offers.urls')),
    path('contact',include(router.urls)),
    path('questions/', include('Question.urls')),  


    # path('contact',ContactMessage.as_view(),name='contact'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
