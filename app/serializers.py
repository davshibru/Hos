from rest_framework import serializers
from .models import Doctors, Reception
from rest_framework.validators import UniqueTogetherValidator


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reception
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Reception.objects.all(),
                fields=['doctor', 'time', 'date'],
                message='Работает'
            )
        ]













    # def create(self, validated_data):
    #     return Reception.objects.create(**validated_data)
    #
    # def validate(self, value):
    #     data = Doctors.objects.all()
    #     doctors = data['doctor']
    #
    #     if doctors.get(1) == value['doctor']:
    #         raise serializers.ValidationError("Bad doctor")
    #     return value
