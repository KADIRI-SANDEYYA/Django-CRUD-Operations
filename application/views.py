from django.shortcuts import render, redirect
# from application.forms import EmployeeForm
from application.models import EmployeeModel
from django.db.models import Sum




def employee_list(request):
    employee_data = EmployeeModel.objects.all()
    total_employees = EmployeeModel.objects.count()
    total_departments = EmployeeModel.objects.values('department').distinct().count()
    monthly_payroll = EmployeeModel.objects.aggregate(total_salary=Sum('salary'))['total_salary'] or 0
    monthly_payroll = round(monthly_payroll/100000)
    return render(
        request,
        'employee_list.html',
        {
            'employee_data': employee_data,
            'total_employees': total_employees,
            'total_departments': total_departments,
            'monthly_payroll': monthly_payroll,
        }
    )