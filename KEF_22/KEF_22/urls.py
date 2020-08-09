"""KEF_22 URL Configuration

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
from django.urls import path, include
from django.conf import settings #new import
from django.conf.urls.static import static #new import

from KEF_22.KEF_App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('teacher/assesment/', views.take_assesment, name='take_assesment'), #new changes
    path('upload/', views.upload, name='upload'),
    path('getscore/', views.cal_score, name='calscore'),
]

#new changes
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
