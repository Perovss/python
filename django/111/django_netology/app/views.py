from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Weapon
from .serializers import WeaponSerializers

# @api_view(['GET'])
# def demo(request):
#     weapons = Weapon.objects.all()
#     ser = WeaponSerializers(weapons, many = True)
#     # data = {'message': 'Hello'}
#     return Response(ser.data)

# @api_view(['GET','POST'])
# def demo(request):
#     if request.method =='GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializers(weapons, many = True)
#         # data = {'message': 'Hello'}
#         return Response(ser.data)
#     if request.method =='POST':
#         return Response({'status': 'OK'})

# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializers(weapons, many = True)
#         return Response(ser.data)

#     def post(self, request):
#         return Response({'status': 'OK'})

class DemoView(ListAPIView):
    queryset = weapons = Weapon.objects.all()
    serializer_class = WeaponSerializers
    def post(self, request):
        return Response({'status': 'OK'})

class WeapomView(RetrieveAPIView):
    queryset = weapons = Weapon.objects.all()
    serializer_class = WeaponSerializers
    