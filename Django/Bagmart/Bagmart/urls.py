"""
URL configuration for Bagmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from django.views.generic import TemplateView  
from home.views import registration , customerlogin , main, shop, Aboutus
from home.views import logout_view 
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , TemplateView.as_view(template_name='index.html'), name='index' ), 
    path('customerlogin/', customerlogin, name='customerlogin'),
    path('main/', main, name='main'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('shop/', shop, name='shop'),
    path('Aboutus/', Aboutus, name='Aboutus'),
         
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
