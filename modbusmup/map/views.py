from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer


class UserRegistrationApiView(APIView):
    # serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
