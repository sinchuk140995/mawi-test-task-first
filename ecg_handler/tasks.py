from __future__ import absolute_import, unicode_literals
from celery import task

from . import models


@task()
def math_expectation_and_dispersion(electrocardiogram_id):
    try:
        ecg = models.Electrocardiogram.objects.get(pk=electrocardiogram_id)
    except ValidationError:
        return {'message': 'No such electrocardiogram.'}

    stop_index = signals_count = len(ecg.signals)
    step = 500 if signals_count > 500 else signals_count
    start_index = 0
    end_index = start_index + step
    probability_of_values = dict()
    dispersion_of_values = dict()

    while end_index <= stop_index:
        signal_ids = [signal.id for signal in ecg.signals[start_index:end_index]]
        pipeline = [
            {
                "$match": {
                    '_id': {'$in': signal_ids}
                }
            },
            {
                "$group": {
                    "_id": "$value",
                    "count": {"$sum": 1}
                }
            }
        ]
        count_of_values = models.Signal.objects.aggregate(*pipeline)
        for count_of_value in count_of_values:
            value = count_of_value['_id']
            count = count_of_value['count']
            probability_of_values[value] = count / signals_count

        start_index = end_index
        end_index += step
        if end_index > stop_index:
            end_index = stop_index

        if start_index == end_index:
            break

    math_expecation = 0
    for value, probability in probability_of_values.items():
        math_expecation += value * probability

    dispersion = 0
    for value, probability in probability_of_values.items():
        dispersion += probability * pow(value - math_expecation, 2)

    return {
        'math_expecation': math_expecation,
        'dispersion': dispersion,
    }
