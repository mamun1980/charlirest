from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    f_name = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'
    
    def get_f_name(self, obj):
        return obj.full_name[:4]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hello'] = 'Mamun'

        return representation
    
    def to_internal_value(self, data):
        resource_data = data['movie']
        import pdb; pdb.set_trace();

        return super().to_internal_value(resource_data)

    
    def validate(self, attrs):
        if attrs['us_gross'] > attrs['worldwide_gross']:
            raise serializers.ValidationError('worldwide_gross cannot be bigger than us_gross')
        # return super().validate(attrs)
        return attrs

    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('Rating has to between 1 and 10')
        return value
     

"""


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

"""