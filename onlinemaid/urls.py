# onlinemaid urls


from django.contrib import admin
from django.urls import path, include
from webfront.views import index, searchmaid, contactus, shortlisted
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webfront.urls')),   
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
