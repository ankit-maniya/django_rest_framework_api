# GenericcAPIView and Model Mixin


from .models import Student
from .serializers_models import StudentModelSerializers

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentListAndCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetriveUpdateAndDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
