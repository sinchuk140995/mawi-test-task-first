from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from . import models


class ElectrocardiogramViewSet(viewsets.ViewSet):

    # def retrieve(self, request):
    #     return Response('status=status.HTTP_201_CREATED')

    def create(self, request):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
