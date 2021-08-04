from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

# Create your views here.

# Views for Employee
@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employee_detail(request, pk):
    employee = Employee.objects.get(emp_id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employee_create(request):
    serializer = EmployeeSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def employee_update(request, pk):
    employee = Employee.objects.get(emp_id=pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def employee_delete(request, pk):
    employee = Employee.objects.get(emp_id=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Views for Department
@api_view(['GET'])
def department_list(request):
    department = Department.objects.all()
    serializer = DepartmentSerializer(department, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def department_detail(request, pk):
    department = Department.objects.get(dep_id=pk)
    serializer = DepartmentSerializer(department, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def department_create(request):
    serializer = DepartmentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def department_update(request, pk):
    department = Department.objects.get(dep_id=pk)
    serializer = DepartmentSerializer(department, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def department_delete(request, pk):
    department = Department.objects.get(dep_id=pk)
    department.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)