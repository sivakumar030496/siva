from django.http import Http404
from django.shortcuts import render
import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

class QuoteViewset(viewsets.ViewSet):
    def list(self,request):
        products = Quote.objects.all()
        serializer = QuoteSerializers(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = QuoteSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        product = Quote.objects.get(pk=pk)
        serializer = QuoteSerializers(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self,request,pk=None):
        product = Quote.objects.get(pk=pk)
        serializer = QuoteSerializers(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self,request,pk=None):
        product = Quote.objects.get(pk=pk)
        product.delete()

        return Response('Quote deleted')

class UserAPIView(APIView):
    def get(self,_):
        users = User.objects.all()
        return Response(UserSerializers(users).data)
class UserDetailAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        return Response(UserSerializers(users).data)
class UserDetailAPIView(APIView):
    def get_user(self,pk):
        try:
            User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        user = self.get_user(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

