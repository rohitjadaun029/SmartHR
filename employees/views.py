from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from .models import Employee
from .forms import EmployeeForm


# ==============================
# ADMIN CHECK
# ==============================

def is_admin(user):
    return user.is_superuser or user.is_staff


# ==============================
# DASHBOARD
# ==============================

@login_required
def dashboard(request):

    if not is_admin(request.user):
        return redirect('dashboard')

    employees = Employee.objects.all()

    total_employees = employees.count()

    total_payroll = employees.aggregate(
        total=Sum('salary')
    )['total'] or 0

    today = timezone.localdate()

    new_this_month = employees.filter(
        joining_date__year=today.year,
        joining_date__month=today.month
    ).count()

    context = {
        'employees': employees,
        'total_employees': total_employees,
        'total_payroll': total_payroll,
        'new_this_month': new_this_month,
    }

    return render(
        request,
        'employees/dashboard.html',
        context
    )


# ==============================
# ADD EMPLOYEE
# ==============================

@login_required
def add_employee(request):

    if not is_admin(request.user):
        return redirect('dashboard')

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employees/add_employee.html',
        {
            'form': form
        }
    )


# ==============================
# EDIT EMPLOYEE
# ==============================

@login_required
def edit_employee(request, employee_id):

    if not is_admin(request.user):
        return redirect('dashboard')

    employee = get_object_or_404(
        Employee,
        employee_id=employee_id
    )

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        'employees/edit_employee.html',
        {
            'form': form,
            'employee': employee
        }
    )


# ==============================
# DELETE EMPLOYEE
# ==============================

@login_required
def delete_employee(request, employee_id):

    if not is_admin(request.user):
        return redirect('dashboard')

    employee = get_object_or_404(
        Employee,
        employee_id=employee_id
    )

    if request.method == 'POST':

        employee.delete()

        return redirect('dashboard')

    return render(
        request,
        'employees/delete_employee.html',
        {
            'employee': employee
        }
    )


# ==============================
# LOGIN
# ==============================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'employees/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'employees/login.html'
    )


# ==============================
# LOGOUT
# ==============================

def logout_view(request):

    logout(request)

    return redirect('login')