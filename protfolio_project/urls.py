

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protfolio.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('comments/', include('django_comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)