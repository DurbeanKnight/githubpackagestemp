from django.shortcuts import render

from rest_framework import serializers
from .models import Employee

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'company', 'photo')




class EmployeeListAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

