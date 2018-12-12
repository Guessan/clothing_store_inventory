from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$/', views.index, name='index'),
    url(r'^homepage/', views.homepage, name='homepage'),
    url(r'^about/', views.about, name='about'),
    url(r'^brand/', views.brand),
    url(r'^color/', views.brand),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    

]