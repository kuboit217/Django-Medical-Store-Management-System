from rest_framework import serializers
from DjangoMedicalApp.models import Company , CompanyBank

#tạo lớp Company
class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

#tạo lớp company bank
class CompanyBankSerliazer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'

    #tạo khóa ngoại lấy info compnay
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response