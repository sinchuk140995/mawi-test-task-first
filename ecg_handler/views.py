from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models


class ElectrocardiogramCreateView(APIView):

    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
