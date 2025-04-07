from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from main.views import page_not

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls', namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

handler404 = page_not

admin.site.site_header = "Привет, парень"
admin.site.index_title = "О-да, измени в этой грязной сучке что-нибудь..."