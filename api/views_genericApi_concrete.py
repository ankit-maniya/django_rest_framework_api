# GenericcAPIView and Model Mixin


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers


class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
