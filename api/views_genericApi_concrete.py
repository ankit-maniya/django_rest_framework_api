# GenericcAPIView and Model Mixin


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'stu_view'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'name']


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stu_create'


class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stu_retrive'


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stu_update'
