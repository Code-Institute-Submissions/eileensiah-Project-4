# onlinemaid urls


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', include('webfront.urls')), 
    path('webback/', include('webback.urls')), 
    path('agency/', include('agency.urls')), 
    path('product_cart/', include('product_cart.urls')),
    path('shortlisted_cart/', include('shortlisted_cart.urls')),
    path('payment/', include('payment.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
