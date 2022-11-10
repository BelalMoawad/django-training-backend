from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework import status, permissions
from musicPlatform.permissions import IsAuthenticatedorReadOnly, IsSameUserOrReadOnly

class UserView(APIView) :
    # permission_classes = [IsAuthenticatedorReadOnly&IsSameUserOrReadOnly]
    permission_classes = [permissions.AllowAny]
    def get(self, request, pk) :
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk) :
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    def patch(self, request, pk) :
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)    