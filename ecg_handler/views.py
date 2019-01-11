from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mongoengine.errors import ValidationError

from . import models
from . import tasks


class ElectrocardiogramCreateView(APIView):

    def post(self, request):
        electrocardiogram = models.Electrocardiogram(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name')
        )
        try:
            electrocardiogram.save()
        except ValidationError as error:
            return Response(error.message, status=status.HTTP_400_BAD_REQUEST)

        return Response(electrocardiogram.to_json(), status=status.HTTP_201_CREATED)


class SignalCreateView(APIView):

    def post(self, request, *args, **kwargs):
        electrocardiogram_id = request.data.get('electrocardiogram_id', '')
        try:
            electrocardiogram = models.Electrocardiogram.objects.get(pk=electrocardiogram_id)
        except ValidationError as error:
            return Response(error.message, status=status.HTTP_400_BAD_REQUEST)

        if electrocardiogram.end_date:
            error_message = 'Electrocardiogram is over.'
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        received_signal_values = request.data.get('signals', [])
        number_signal_values = []
        invalid_signal_values = []
        for value in received_signal_values:
            if type(value) == int:
                number_signal_values.append(value)
            elif type(value) == str and value.isdigit():
                number_signal_values.append(int(value))
            else:
                invalid_signal_values.append(value)

        if len(invalid_signal_values) > 0:
            error_message = 'Values {} is invalid.'.format(','.join(invalid_signal_values))
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        signals = [models.Signal(value=value) for value in number_signal_values]
        try:
            saved_signals = models.Signal.objects.insert(signals)
        except ValidationError as error:
            return Response(error.message, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('last_portion', False):
            electrocardiogram.end_date = timezone.now()

        electrocardiogram.signals.extend(saved_signals)
        electrocardiogram.save()
        return Response(status=status.HTTP_201_CREATED)
