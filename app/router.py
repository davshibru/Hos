from rest_framework import routers
from .views import DoctorViewSet, ReceptionViewSet

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('receptions', ReceptionViewSet)
