
from django.contrib import admin
from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('howework/',views.howework,name='work'),
    path('footer/',views.footer,name='footer'),
    path('services/<id>',views.ServicePro),
    path('base/',views.base,name='base'),
    path('serviceTemp/<id>',views.serviceTemp,name='serviceTemp'),
    path('freetrial',views.freeTrial,name='freetrial'),
    path('pricing',views.pricing,name='pricing'),
    path('ordernow',views.ordernow,name='ordernow'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)