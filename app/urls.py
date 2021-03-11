from django.contrib import admin
from django.urls import path, include
from .views import ReceptionView

app_name = "reception"

urlpatterns = [
    path('reception/', ReceptionView.as_view()),
]












# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', DoctorView.as_view())
# ]
