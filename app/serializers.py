from rest_framework import serializers
from .models import Doctors, Reception, TimesOfWork
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimesOfWork
        fields = '__all__'

class ReceptionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reception
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reception
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Reception.objects.all(),
                fields=['doctor', 'time', 'date'],
                message='Выберете другого доктора, дату или время'
            )
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user













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
