from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main_website import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('escola/', views.school, name="school"),
    path('diferenciais/', views.diferentials, name="diferentials"),
    path('visitacao/', views.visitation, name="visitation"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('success/', views.success, name="success"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #That will create a path to see the images in the browser