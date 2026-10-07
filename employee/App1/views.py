
from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee, Department, Company


def display(request):
    data = Employee.objects.all()
    return render( request, "empdata.html",{'employdata': data})


def addEmpData(request):

    dep_data = Department.objects.all()
    company_data = Company.objects.all()

    if request.method == "POST":
        name = request.POST.get('nm')
        email = request.POST.get('em')
        age = request.POST.get('ag')
        salary = request.POST.get('sal')

        # Form se ID aa rahi hai
        department_id = request.POST.get('dept')
        company_id = request.POST.get('com')

        address = request.POST.get('add')

        # ID ko actual object me convertS karo
        department = Department.objects.get(id=department_id)
        company = Company.objects.get(id=company_id)

        emp = Employee(
            name=name,
            age=age,
            email=email,
            salary=salary,
            department=department,
            Company=company,
            address=address
        )

        emp.save()

        msg = "Data Saved Successfully"

        return render(request,'form.html', {'msg': msg,'dep_data': dep_data,'company_data': company_data})
    return render(request, 'form.html', { 'dep_data': dep_data, 'company_data': company_data  } )


def updateEmpData(request, id):
    emp = get_object_or_404(Employee, id=id)

    dep_data = Department.objects.all()
    company_data = Company.objects.all()

    if request.method == 'POST':

        emp.name = request.POST.get('nm')
        emp.email = request.POST.get('em')
        emp.age = request.POST.get('ag')
        emp.salary = request.POST.get('sal')
        emp.address = request.POST.get('add')

        department_id = request.POST.get('dept')
        company_id = request.POST.get('com')

        if department_id:
            emp.department = Department.objects.get(id=department_id)

        if company_id:
            emp.Company = Company.objects.get(id=company_id)

        emp.save()
        return redirect('display')
    
        msg = "Employee Data Updated Successfully"

        return render(
            request,
            'editform.html',
            {
                'emp': emp,
                'dep_data': dep_data,
                'company_data': company_data,
                'msg': msg
            }
        )

    return render(request,'editform.html',{'emp': emp,'dep_data': dep_data,   'company_data': company_data } )
def deleteEmpData(request,id):
    emp = get_object_or_404(Employee,id=id)
    emp.delete()
    return redirect('display')

