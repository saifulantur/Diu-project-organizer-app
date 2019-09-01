
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projectapp.urls")),
    
]
handler404 = 'projectapp.views.error_404_view'

#Customizing Admin site
admin.site.site_header = 'Project Organizer'
admin.site.index_title = 'Hi! Welcome to project'
admin.site.site_title = 'Control Panel'

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

