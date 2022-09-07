# ViewSet and Model Serializer


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
