# ViewSet and Model Serializer


from .models import Student
from .serializers_models import StudentModelSerializers
from .permission_custome import MyPermission
from .throttling import JackRateThrottle


from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication, SessionAuthentication, TokenAuthentication
)
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, AllowAny,
    IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions] # we can manage user permission from admin
    # we can manage user permission from admin
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class StudentModelViewSetCustome(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
    # Token based CRUD operations
    # authentication_classes = [TokenAuthentication]
    # JWT authentication
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    throttle_classes = [JackRateThrottle]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [MyPermission] # Custome Permission created
