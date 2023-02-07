from rest_framework.serializers import ModelSerializer
from .models import Student
from rest_framework import serializers as serializer


class StudentSerializer(serializer.ModelSerializer):
    id = serializer.IntegerField(required=False)

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        print('Created record ', validated_data, " with i d", validated_data.get('id'), " successfully")
        return super().create(validated_data)

    def validate_id(self,value):

        if Student.objects.get(id) == None:
            raise serializer.ValidationError("Id Does not exist")
        return True

