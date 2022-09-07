# GenericcAPIView and Model Mixin


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stu_view'


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
