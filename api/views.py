import pandas as pd
from django.shortcuts import render
from .models import Company, Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CompanySerializers, EmployeeSerializers
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class UploadFile(APIView):
    
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded."}, status=HTTP_400_BAD_REQUEST)
        
        df = pd.read_excel(file)
        # print(df.head(2))
        unique_companies = df["COMPANY_NAME"].unique()
        companies_objs = [Company(company_name=name) for name in unique_companies]
        # print(companies_objs)
        Company.objects.bulk_create(companies_objs, ignore_conflicts=True)                
        
        # for i in companies_id_value:
        #     print(i.company_name, i.id)        
        companies_id_value = {detail.company_name: detail.id for detail in Company.objects.filter(company_name__in=unique_companies)}        
        print(companies_id_value)
        
        # Validated till here and found ok

        # work start for Employee data
        
        emp_data = []
        if_error_found = []
        
        for index, row in df.iterrows():
            # print(index, row)
            row_data = {
                "company": row["COMPANY_NAME"],
                "employee_id": row["EMPLOYEE_ID"],
                "first_name": row["FIRST_NAME"],
                "last_name": row["LAST_NAME"],
                "phone_number": row["PHONE_NUMBER"],
                "salary": row["SALARY"],
                "manager_id": row["MANAGER_ID"],
                "department_id": row["DEPARTMENT_ID"],
            }            
            serializer = EmployeeSerializers(data=row_data)
            # print(serializer.is_valid())

            if serializer.is_valid():
                validated = serializer.validated_data                
                emp_data.append(Employee(**validated))
            else:
                if_error_found.append({index: serializer.errors})

        if if_error_found:
            return Response({"error": if_error_found}, status=HTTP_400_BAD_REQUEST)

        # If everything is fine as expected then create bulk entries and return 201 response.
        Employee.objects.bulk_create(emp_data)
        
        return Response({"Success": "Recoreds created successfully."}, status=HTTP_201_CREATED)                    

