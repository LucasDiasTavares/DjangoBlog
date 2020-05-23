from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, search, post_create , post_update, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/', blog, name='post-list'),
    path('seach/', search, name='search'),
    path('post/<id>/', post, name='post-detail'),
    path('post-create/', post_create, name='post-create'),
    path('post-update/<id>/', post_update, name='post-update'),
    path('post-delete/<id>/', post_delete, name='post-delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
