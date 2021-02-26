import io
from .models import Students
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializers

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


@csrf_exempt
# function based view
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print('this is byte io data', stream)
        pythondata = JSONParser().parse(stream)
        print('this is python data', pythondata)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Students.objects.get(id=id)
            print(stu)
            serializer = StudentSerializers(stu)
            print(serializer)
            json_data = JSONRenderer().render(serializer.data)
            print(json_data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Students.objects.all()
        print(stu)
        serializer = StudentSerializers(stu, many=True)
        print(serializer)
        json_data = JSONRenderer().render(serializer.data)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        strem = io.BytesIO(json_data)
        pythondata = JSONParser().parse(strem)
        id = pythondata.get('id')
        stu = Students.objects.get(id=id)


        #partial update
        '''when we can update only partial data at time we use (partial= True) below example are given
           e.g:- serializer = StudentSerializers(stu, data=pythondata, partial=True)
           given only partial data from front end or backend'''



        #full update
        serializer = StudentSerializers(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        strem = io.BytesIO(json_data)
        python_data = JSONParser().parse(strem)
        id = python_data.get('id')
        stu = Students.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data deleted!!'}


        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


