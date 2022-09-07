from rest_framework import serializers
from .models import Student


class StudentModelSerializers(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True) # for making read only field

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['id']
        extra_kwargs = {'id': {'read_only': True}}

    def validate_roll(self, value):
        if value < 11:
            raise serializers.ValidationError(
                f'This {value} Number is Not Allowed!')
        return value
