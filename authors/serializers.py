from rest_framework import serializers
from datetime import date
from .models import Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality']

    def validate(self, data):

        birth_date = data.get('birth_date')
        if birth_date and birth_date > date.today():
            raise serializers.ValidationError({"birth_date": "Tug‘ilgan sana kelajakdagi sana bo‘lishi mumkin emas."})


        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if first_name and last_name and first_name.lower() == last_name.lower():
            raise serializers.ValidationError({"non_field_errors": "Ism va familiya bir xil bo‘lmasligi kerak."})

        return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']

        def validate(self, data):

            if not data.get("name") or len(data["name"]) < 3:
                raise serializers.ValidationError({"name": "Nom kamida 3 ta belgidan iborat bo‘lishi kerak!"})

            if not data.get("description") or len(data["description"]) < 10:
                raise serializers.ValidationError(
                    {"description": "Tavsif kamida 10 ta belgidan iborat bo‘lishi kerak!"})

            return data
