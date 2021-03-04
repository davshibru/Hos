from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Doctors, Reception
from .serializers import DoctorsSerializer, ReceptionSerializer

# class DoctorView(APIView):
#
#     def get(self, request):
#         doctors = Doctors.objects.all()
#         serializer = DoctorsSerializer(doctors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = DoctorsSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#         return Response(serializer.data)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

    # def create(self, request):
    #     assets = []
    #     farming_details = {}
    #     datas = request.data
    #
    #     if datas.doctor == 1:
    #         pass
    #     else:
    #         datas.save()
 #kjsdhfklsdgjshfjlgskhkfdhgkldagkjsjdfhglkdfhgskd;


#https://drive.google.com/file/d/1wxNibWBdR1kjPlfVFhdbyDFFbG8idxpG/view