from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    User = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if email and password and first_name and last_name:
        try:
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error': 'An error occurred while registering the user.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Please provide all required information.'}, status=status.HTTP_400_BAD_REQUEST)
