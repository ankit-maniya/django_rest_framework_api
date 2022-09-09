from dataclasses import field
from rest_framework import serializers
from .models import Singer, Song, Student


class StudentModelSerializers(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True) # for making read only field

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city', 'passby']
        # read_only_fields = ['id']
        extra_kwargs = {'id': {'read_only': True}}

    def validate_roll(self, value):
        if value < 11:
            raise serializers.ValidationError(
                f'This {value} Number is Not Allowed!')
        return value


class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']
        read_only_fields = ['id']


class SingerModelSerializer(serializers.ModelSerializer):
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #  songs = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )

    # songs = serializers.HyperlinkedIdentityField(view_name='song-detail')
    songs = SongModelSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Singer
        read_only_fields = ['id']
        fields = ['id', 'gender', 'name', 'songs']
