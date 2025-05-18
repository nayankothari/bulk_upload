from rest_framework import serializers
from .models import (Company, Employee)


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "_all__"


class EmployeeSerializers(serializers.ModelSerializer):
    # company = serializers.CharField(write_only=True)
    company = serializers.SlugRelatedField(
        slug_field='company_name',  # lookup by name
        queryset=Company.objects.all()
    )
    class Meta:
        model = Employee
        fields = ["company", "employee_id", "first_name", "last_name", "phone_number", "salary",
                  "manager_id", "department_id"]
        
    