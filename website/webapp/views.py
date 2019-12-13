from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from .serailizers import employeesSerializer
from rest_framework import filters
from rest_framework import generics
from django.db.models import Sum,Avg,Max,Min,Count,F,Q

# Create your views here.
class employeeList(APIView):

    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class userList(generics.ListAPIView):
    queryset = employees.objects.all()
    serializer = employeesSerializer(queryset,many=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'salary']
    ordering = ['salary']

 class CustomSearchFilter(filters.SearchFilter):
        def get_search_fields(self, view, request):
            if request.query_parms.get('type_only'):
                return ['type']
            return super(CustomSearchFilter,self).get_search_fields(view,request)
          def get_salary(self,obj):
              total_salary=employees.objects.all().avg(total_salary=Avg('salary'))
              return total_salary['total_salary']



