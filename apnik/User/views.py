from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CustomerList(APIView):
	def get(self, request):
		customers = User.objects.all()
		serializer = CustomerSerializer(customers, many = True)
		return Response(serializer.data)


class CustomerEdit(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)