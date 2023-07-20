from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kegiatan_list/', views.kegiatan_list, name='kegiatan_list'),
    path('create/', views.kegiatan_create, name='kegiatan_create'),
    path('update/<int:pk>/', views.kegiatan_update, name='kegiatan_update'),
    path('delete/<int:pk>/', views.kegiatan_delete, name='kegiatan_delete'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
