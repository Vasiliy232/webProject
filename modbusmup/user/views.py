from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics


class LoginUserApiView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        user = request.user
        if user.is_authenticated:
            return Response({'detail': 'You are already logged in.'})

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'detail': 'Account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserApiView(generics.GenericAPIView):
    @staticmethod
    def post(request):
        user = request.user
        if user.is_authenticated:
            request.user.auth_token.delete()
            return Response({'detail': 'Logged out successfully.'})
        else:
            return Response({'detail': 'User not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)
