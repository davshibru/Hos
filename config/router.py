from rest_framework import routers
from app.views import DoctorViewSet, ReceptionViewSet

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('receptions', ReceptionViewSet)