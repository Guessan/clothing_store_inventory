from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', views.homepage, name='homepage')
]