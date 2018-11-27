from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.home,name='hom'),
    url(r'^hero/(\d+)',views.hero,name ='hero'),
    url(r'^upload/',views.upload,name ='upload')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)