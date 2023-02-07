import django.db.models
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import StudentSerializer
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.views import APIView


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        incoming_data = request.data
        incoming_python_data = json.loads(json.dumps(incoming_data))
        student_deserialized_data = StudentSerializer(data=incoming_python_data)
        if student_deserialized_data.is_valid():
            student_deserialized_data.save()
            print(type(student_deserialized_data.validated_data))
            return Response({'msg': 'Welcome you on board',
                             'name': student_deserialized_data.validated_data.get('name')}, content_type='application'
                                                                                                         '/json')
        else:
            print(student_deserialized_data.errors)
            return Response({'msg': "Failed to register...PLease try again",
                             'error': student_deserialized_data.errors}, content_type='application/json')
    if request.method == 'GET':
        incoming_id = request.data.get('id')
        student_query_set = Student.objects.get(id=incoming_id)
        student_serialized = StudentSerializer(student_query_set)
        return Response(student_serialized.data, content_type='application/json')


class StudentApi(APIView):
    def get(self, request, pk=None):
        if request.method == "GET":
            if pk is not None:
                print("PK is not None")
                id = pk
                try:
                    queryset_result = Student.objects.get(pk=id)
                except Student.DoesNotExist:
                    return Response({'error': "ID Does not exist"}, content_type='application/json')
                print(type(queryset_result))
                student_serialized = StudentSerializer(queryset_result)
                print(type(student_serialized))
                return Response(student_serialized.data, content_type='application/json')
            else:
                print("PK is None")
                queryset_result = Student.objects.all()
                print(type(queryset_result))
                student_serialized = StudentSerializer(queryset_result, many=True)
                print(type(student_serialized))
                return Response(student_serialized.data, content_type='application/json')
