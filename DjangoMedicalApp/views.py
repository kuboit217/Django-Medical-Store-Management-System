from DjangoMedicalApp.serializers import CompanySerialzer
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from DjangoMedicalApp.models  import Company
from DjangoMedicalApp.serializers import CompanySerialzer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerialzer
