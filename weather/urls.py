from django.urls import path,include
from .views import DescriptionViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',DescriptionViewsets)





urlpatterns = [
    path('', include(router.urls)),
]
