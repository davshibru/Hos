from rest_framework import routers
from .views import DoctorViewSet, ReceptionViewSet, ReceptionDetailView, TimeViewSet

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('receptions', ReceptionViewSet, basename='receptions')
router.register('time', TimeViewSet)