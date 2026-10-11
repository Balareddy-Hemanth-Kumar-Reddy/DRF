from rest_framework import serializers
from .models import Person

# class PersonSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
    
class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields =['id', 'name', 'age', 'email']  



        # def create(self, validated_data):
        #     return Person.objects.create(**validated_data)

        # def update(self, instance, validated_data):
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.age = validated_data.get('age', instance.age)
        #     instance.email = validated_data.get('email', instance.email)
        #     instance.save()
        #     return instance

