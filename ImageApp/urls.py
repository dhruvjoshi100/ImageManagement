from ImageApp import view
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'photos', view.PhotoViewSet)
router.register(r'users', view.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
