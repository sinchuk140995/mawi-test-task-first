from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mongoengine.errors import ValidationError

from . import models


class ElectrocardiogramCreateView(APIView):

    def post(self, request):
        electrocardiogram = models.Electrocardiogram(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
        )
        try:
            electrocardiogram.save()
        except ValidationError as error:
            return Response(error.message, status=status.HTTP_400_BAD_REQUEST)

        return Response(electrocardiogram.to_json(), status=status.HTTP_201_CREATED)
