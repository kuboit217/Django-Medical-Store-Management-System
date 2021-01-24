from django.shortcuts import render
from rest_framework import viewsets, generics


# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


from DjangoMedicalApp.models  import Company , CompanyBank
from DjangoMedicalApp.serializers import CompanySerliazer , CompanyBankSerliazer

#viewset company
class CompanyViewSet(viewsets.ViewSet):
    #tạo và kiểm tra token
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    #hàm list thông tin company
    def list(self,request):
        compnay = Company.objects.all()
        serializer = CompanySerliazer(compnay, many=True, context={'request':request}) 
        reponse_dict = {'error':False, 'message':'All Company List Data','data':serializer.data}
        return Response(reponse_dict)
    
    #hàm create company
    def create(self,request):
        try:
            serializer = CompanySerliazer(data = request.data,context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            dict_reponse = {'error':False, 'message':'Company Data Save Susscesfully'}
        except:
            dict_reponse = {'error':True, 'message':'Error During Saving Company Data'} 
        return Response(dict_reponse)   

    #hàm update company
    def update(self,request,pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk) 
            serializer = CompanySerliazer(company, data = request.data, context={'request':request})
            serializer.is_valid()
            serializer.save()    
            dict_reponse = {'error':False, 'message':'Susscesfully Update Company Data'}   
        except:
            dict_reponse = {'error':False, 'message':'Error During Update Company Data'}    
        return Response(dict_reponse)  

#viewset CompanyBank.
class CompanyBankViewSet(viewsets.ViewSet): 
    #tạo và kiểm tra token
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #tạo hàm create company bank
    def create(self,request):
        try:
            serializer = CompanyBankSerliazer(data = request.data,context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            dict_reponse = {'error':False, 'message':'Company Bank Data Save Susscesfully'}
        except:
            dict_reponse = {'error':True, 'message':'Error During Saving Company Bank Data'} 
        return Response(dict_reponse)  
    
    #tạo hàm list company bank
    def list(self,request):
        compnaybank = CompanyBank.objects.all()
        serializer = CompanyBankSerliazer(compnaybank, many=True, context={'request':request}) 
        reponse_dict = {'error':False, 'message':'All Company Bank List Data','data':serializer.data}
        return Response(reponse_dict)

    #hàm lấy 1 thông tin vào data trong CompanyBank
    def retrieve(self,request,pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk = pk)
        serializer = CompanyBankSerliazer(companybank,context={'request':request})
        reponse_dict = {'error':False, 'message':'Single Data Fetch','data':serializer.data}
        return Response(reponse_dict)

    #hàm update compnay bank 
    def update(self,request,pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk = pk)
            serializer = CompanyBankSerliazer(companybank,data = request.data,context={'request':request})
            serializer.is_valid()
            serializer.save()
            dict_reponse = {'error':False, 'message':'Data has Been Update'}
        except:
            dict_reponse = {'error':True, 'message':'Data Company Bank Cannot Update'}
        return Response(dict_reponse)

#class xem tên bank
class CompanyNameViewset(generics.ListAPIView):
    serializer_class = CompanySerliazer
    def get_queryset(self):
        name = self.kwargs['name']
        return Company.objects.filter(name=name)






company_list = CompanyViewSet.as_view({'get':'list'})
company_create = CompanyViewSet.as_view({'post':'create'})
company_update = CompanyViewSet.as_view({'put':'update'})
