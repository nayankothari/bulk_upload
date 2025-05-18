from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    company_name = models.CharField(max_length=300, null=False, blank=False, unique=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company details"


class Employee(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    employee_id = models.IntegerField(blank=False, null=True)
    first_name = models.CharField(max_length=256, null=True, blank=False)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    manager_id = models.IntegerField(null=True, blank=True) # Here i can map manager tagle relation 
    department_id = models.IntegerField(null=True, blank=True) # Here i can map department table relations 

    class Meta:
        verbose_name_plural = "Employee Mastre"


    def __str__(self):
        return str(self.employee_id)