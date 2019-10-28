from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create/profile/',views.create_profile, name='create-profile'),
    path('home/', views.home, name='home'),
    path('add/hood/', views.add_hood, name='add_hood'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)