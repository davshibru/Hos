from django.contrib import admin
from django.urls import path, include
from .views import DoctorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', DoctorView.as_view())
]
