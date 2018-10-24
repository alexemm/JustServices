"""JustServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
#=======
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
#>>>>>>> a12aa38c2b414a10edd9c4391940eee2708e4fcc

urlpatterns = [
    path('index/',include('pictures.urls')),
    path('admin/', admin.site.urls),
#<<<<<<< HEAD
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#=======
    path('', include('portal.urls', namespace='portal')),
    path('pictures/', include('pictures.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#>>>>>>> a12aa38c2b414a10edd9c4391940eee2708e4fcc
