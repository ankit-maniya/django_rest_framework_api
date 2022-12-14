from rest_framework import serializers
from .models import Student


def start_with_r(value):
    if value[0].lower() == 'r':
        raise serializers.ValidationError(
            f'Starting with {value[0]} is not allowed!')
    return value


class StudentSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    passby = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.passby = validated_data.get('passby', instance.passby)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value > 11:
            raise serializers.ValidationError('This Number is Not Allowed!')
        return value

    def validate_city(self, value):
        if value in ['jammu', 'Sihor']:
            raise serializers.ValidationError(f'This {value} is Not Allowed!')
        return value
