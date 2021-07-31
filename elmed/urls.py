"""elmed URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from elmed.views import AboutView, ContactView, home
from os import getenv

admin.site.site_header = 'ELMED.AZ ADMIN PANELI'

urlpatterns = [
    path('%s/' % getenv('ADMIN_URL'), admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('haqqimizda/', AboutView.as_view(), name='about'),
    path('elaqe/', ContactView.as_view(), name='contact'),
    path('sobeler/', include('departament.urls')),
    path('hekimler/', include('doctor.urls')),
    path('bloq/', include('blog.urls')),
    path('qeydiyyat/', include('appointment.urls')),
)
