from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView
from health import views
from health.admin import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('health.urls')),
    path('logout/',views.logout_request,name='logout'),
    path('login/',views.login_request,name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
