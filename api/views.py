from functools import partial
import io
import re

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .serializers import StudentSerializers
from .models import Student

# Model Object - Single Student Data


def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializers(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set - All Student Data


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    return JsonResponse(serializer.data, safe=False)


def return_python_data(json_data):
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    return python_data


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body

        python_data = return_python_data(json_data)
        serializer = StudentSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    res = {'msg': 'Data Not Created'}
    return JsonResponse(res)


def student_fetch_by_id(request):
    if request.method == 'GET':
        json_data = request.body
        python_data = return_python_data(json_data)

        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def student_insert(request):
    if request.method == 'POST':
        json_data = request.body
        python_data = return_python_data(json_data)
        serializer = StudentSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'message': 'Student Added Successfully'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    return JsonResponse({'message': 'data not created!'})


@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        python_data = return_python_data(json_data)

        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(
                stu, data=python_data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Data Updated!!"})
            return JsonResponse(serializer.errors)
        return JsonResponse({"message": "Please send Id appropriate!"})
    return JsonResponse({"message": "Data not updated!"})

@csrf_exempt
def student_delete(request):
    if request.method == "DELETE":
        json_data = request.body
        python_data = return_python_data(json_data)

        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete();

            return JsonResponse({ "message": "Student Deleted Successfully!" })
    return JsonResponse({"message": "Student is not Deleted!"})