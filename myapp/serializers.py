from .models import Students
from rest_framework import serializers


class StudentSerializers(serializers.Serializer):

    e_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    branch = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.e_no = validated_data.get('e_no', instance.e_no)
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        instance.branch = validated_data.get('branch', instance.branch)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

