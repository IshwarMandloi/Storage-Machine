from django.contrib import admin  
from django.urls import path  
from product import views  
from django.conf.urls import url,include
from django.urls import include, path

urlpatterns = [  
    path('',views.home,name='home'), 
    path('using/',views.using,name='using'),
    path('download/',views.download,name='download'), 
    path('business/',views.business,name='business'),    
    path('admin/', admin.site.urls),  
    path('account/',include('account.urls')),
    path('drive/',include('drive.urls')),
       
] 