"""Crypters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPage, name='landing_page'),
    path('customer/', include('customer.urls', namespace='customer')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('bank/', include('bank.urls', namespace='bank')),
    path('government/', include('government.urls', namespace='government')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
