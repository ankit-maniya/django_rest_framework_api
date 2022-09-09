from rest_framework import viewsets
from .models import Singer, Song
from .serializers_models import SongModelSerializer, SingerModelSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerModelSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer

