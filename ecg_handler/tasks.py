from __future__ import absolute_import, unicode_literals
from celery import task

from . import models


@task()
def math_expectation_and_dispersion():
    pipeline = [
        {
            "$group": {
                "_id": "$value",
                "count": {"$sum": 1}
            }
        }
    ]
    count_of_values = models.Signal.objects.aggregate(*pipeline)
    signals_count = len(models.Signal.objects)
    probability_of_values = dict()
    for count_of_value in count_of_values:
        value = count_of_value['_id']
        count = count_of_value['count']
        probability_of_values[value] = count / signals_count

    math_expecation = 0
    for value, probability in probability_of_values.items():
        math_expecation += value * probability

    dispersion_of_values = dict()
    for value in probability_of_values.keys():
        dispersion_of_values[value] = pow(value - math_expecation, 2)

    return {
        'math_expecation': math_expecation,
        'dispersion_of_values': dispersion_of_values,
    }
