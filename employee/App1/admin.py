from django.contrib import admin
from .models import Employee
from .models import Company,Department

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','age','salary','department','address','Company')
    search_fields = ('name','email')
    ordering = ('id',)
    list_filter = ('Company',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','location','branch_num')
    search_fields = ('name','branch_num')
    ordering = ('id',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
   list_display=('id','name','phone') 
     
    



