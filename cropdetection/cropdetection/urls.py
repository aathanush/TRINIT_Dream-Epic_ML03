"""cropdetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page1',views.webpage1,name='webpage1'),
    path('page2',views.webpage2,name='webpage2'),
    path('process_form', views.process_form, name='process_form'),
    path('form_submit', views.form_submit, name='form_submit'),
    path('page3',views.webpage3,name='webpage3'),
    path('page4',views.webpage4,name='webpage4'),
    path('page5',views.webpage5,name='webpage5'),
    path('page6',views.webpage6,name='webpage6'),
    path('page7',views.webpage7,name='webpage7')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
