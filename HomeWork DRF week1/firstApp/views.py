from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

import datetime

from .models import Store
from firstApp.serializers import CalcSerializer, StoreSerializer


@api_view(http_method_names=['GET'])
def today(request):
    print(datetime.date.today())
    d = datetime.date.today()
    return_dict = {
                'date': f'{d.day}/{d.month}/{d.year}',
                'year': d.year,
                'month': d.month,
                'day': d.day 
                }
    return Response(return_dict)

@api_view(http_method_names=['GET'])
def hello_world(request):
    return Response({'msg': 'Hello World'})

@api_view(http_method_names=['GET'])
def my_name(request):
    name = request.query_params
    return Response(name)

@api_view(http_method_names=['POST'])
def calculator(request):
    serializer = CalcSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.data
    result = None
    if params['action'] == 'minus':
        result = params['number1'] - params['number2']
    elif params['action'] == 'plus':
        result = params['number1'] + params['number2']
    elif params['action'] == 'divide':
        result = params['number1'] / params['number2']
    elif params['action'] == 'multiply':
        result = params['number1'] * params['number2']
    return Response({'result': result})

class StoreApiView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)

