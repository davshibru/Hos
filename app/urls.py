from django.contrib import admin
from django.urls import path, include
from .views import ReceptionViewSet #ReceptionView
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

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
