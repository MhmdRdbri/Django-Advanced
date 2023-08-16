from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import *
from .serializers import *
from blog.models import *
from rest_framework.views import *
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

# @api_view(['GET', 'Put', 'DELETE'])
# def postDetail(request, id):
#     if request.method == 'GET':
#         post = Post.objects.get(pk=id)
#         serializer = postSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer  = postSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         post = get_object_or_404(Post, pk=id)
#         post.delete()
#         return Response({'Detail': 'Item removed successfuly!'}, status=status.HTTP_204_OK)
        

# @api_view(['post','get'])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = postSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = postSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        

# class PostList(ListCreateAPIView):
    
#     permission_classes = [IsAuthenticated]
#     serializer_class = postSerializer
#     queryset = Post.objects.filter(status=True)
    
    
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = postSerializer
    
#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer = postSerializer(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer = postSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         post.delete()
#         return Response({'Detail': 'Item removed successfuly!'}, status=status.HTTP_204_NO_CONTENT)

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = postSerializer
#     queryset = Post.objects.filter(status=True)


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = postSerializer
    queryset = Post.objects.filter(status=True)
    
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  