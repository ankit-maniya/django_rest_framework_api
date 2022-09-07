# ViewSet and Model Serializer


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
