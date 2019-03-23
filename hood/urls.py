from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'), 
    url(r'^create/profile$',views.create_profile, name='create_profile'),
    url(r'^my-profile/',views.my_profile, name='my_profile'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^health',views.health, name='health'),
    url(r'^authorities',views.authorities, name='authorities'),
]     

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)