from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, generics

from .models import Doctors, Reception
from .serializers import ReceptionSerializer, DoctorsSerializer, ReceptionDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#
# class ReceptionView(APIView):
#     def get(self, request):
#         reception = Reception.objects.all()
#         serializer = ReceptionSerializer(reception, many=True)
#         return Response({"reception": serializer.data})

    # def post(self, request):
    #     reception = request.data.get('reception')
    #
    #     serializer = ReceptionSerializer(data=reception)
    #     if serializer.is_valid(raise_exception=True):
    #         reception_saved = serializer.save()
    #         return Response({'success': True})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #
    #     return Response({"success": "Reception '{}' created successfully".format(reception_saved.date)})
    #





















#
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
    permission_classes = (IsAuthenticated, )

class ReceptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReceptionDetailSerializer
    queryset = Reception.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly,)

    # def create(self, request):
    #     assets = []
    #     farming_details = {}
    #     datas = request.data
    #
    #     if datas.doctor == 1:
    #         pass
    #     else:
    #         datas.save()
#  #kjsdhfklsdgjshfjlgskhkfdhgkldagkjsjdfhglkdfhgskd;
#
#
# #https://drive.google.com/file/d/1wxNibWBdR1kjPlfVFhdbyDFFbG8idxpG/view