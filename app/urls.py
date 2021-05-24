from django.contrib import admin
from django.urls import path, include
from .views import ReceptionViewSet, ReceptionDetailView, UserCreate
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/receptions/<int:pk>/', ReceptionDetailView.as_view()),
    path('api/register/', UserCreate.as_view()),

]

app_name = "reception"

# urlpatterns = [
#     path('reception/', ReceptionView.as_view()),
# ]











#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', DoctorView.as_view())
# ]
