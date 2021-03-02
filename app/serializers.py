from rest_framework import serializers
from .models import Doctors, Reception

class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reception
        fields = '__all__'
