
import pdb
from django.shortcuts import render
from django.conf import settings
from django.utils.decorators import method_decorator
from core.decorators import is_authenticated
# from core.middleware import authentication, etl_is_authorized, recommend_is_authorized

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
# from rest_framework_csv.parsers import CSVParser
from rest_framework.decorators import action, parser_classes
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

import uuid

from .serializers import *
from .models import *



class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    # parser_classes = (JSONParser, MultiPartParser)

    @method_decorator(is_authenticated)
    @action(detail=False,  methods=["get"])
    def hello(self, request):
        # pdb.set_trace()
        data = {
            "greetings": "Hello World! This is from get method with authentication...!",
            "EKKPASS_BASE_URL": settings.EKKPASS_BASE_URL
        }
        return Response(data)

    
    @method_decorator(is_authenticated)
    @action(detail=False,  methods=["get"])
    def world(self, request):
        # pdb.set_trace()
        data = {
            "greetings": "Hello World! This is from get method with authentication...!",
            "EKKPASS_BASE_URL": settings.EKKPASS_BASE_URL
        }
        return Response(data)


    @method_decorator(is_authenticated)
    @action(detail=False, methods=['get'])
    def details(self, request):
        # pdb.set_trace()

        data = request.query_params
        return Response(data, status=204)



class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()



"""


class SubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

# class TagsViewSet(viewsets.ModelViewSet):
#     serializer_class = TagsSerializer
#     queryset = Tags.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

"""