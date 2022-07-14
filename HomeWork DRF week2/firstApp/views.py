from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import datetime
from .models import Store
from firstApp.serializers import CalcSerializer, StoreSerializer, StoreNewSerializer


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

class StoreViewSet(ListModelMixin, 
                    # CreateModelMixin, 
                    RetrieveModelMixin, 
                    # UpdateModelMixin, 
                    # DestroyModelMixin, 
                    GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreNewSerializer


class MyStoreViewSet(ModelViewSet):
    serializer_class = StoreNewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Store.objects.filter(owner=user)
        return queryset

    def perform_create(self, serializer):
            serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def mark_as_deactivated(self, request, pk=None):
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class AdminStoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreNewSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['name']
    ordering_fields = []

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'in_review':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

