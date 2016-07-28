from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from grills.views import GrillViewSet

router = DefaultRouter()
router.register(r'grills', GrillViewSet, base_name='grills')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
