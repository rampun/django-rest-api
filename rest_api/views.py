from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .serializers import PostSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# class_based views
from rest_framework.views import APIView
from django.http import Http404

# from rest_framework import generics
# from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.


class PostViewSet(viewsets.ViewSet):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Post.objects.get(pk=id)  # instance of Post class
        except Post.DoesNotExist:
            raise Http404

    def list(self, request):
        posts = Post.objects.all()  # its a query set. so we need to serialize this
        serialzer = PostSerializer(posts, many=True)
        return Response(serialzer.data)

    def create(self, request):
        serialzer = PostSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
