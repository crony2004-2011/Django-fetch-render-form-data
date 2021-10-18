from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import datetime

urlpatterns = [
                  path('/Home/<str:name>', views.home, name='home'),
                  path('/query',views.query, name='query'),
                  #path('/all', views.all, name='all')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
