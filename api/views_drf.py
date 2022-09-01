from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers_models import StudentModelSerializers

from .models import Student

@api_view(['POST', 'GET'])
def hello_word(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentModelSerializers(stu)
            return Response({ "message": "Get called!", 'data': serializer.data }, status= status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentModelSerializers(stu, many=True)
        return Response({ "message": "Get All Student called!", 'data': serializer.data }, status= status.HTTP_200_OK)

    if request.method == 'POST':
        python_data = request.data
        # No need to convert back to python data because it is already converted!
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        serializer = StudentModelSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'Data Added Successfully!' }, status= status.HTTP_200_OK)
        return Response({ "message": "Error occure!", 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)