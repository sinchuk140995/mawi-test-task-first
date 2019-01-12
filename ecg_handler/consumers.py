import json

from channels.generic.websocket import WebsocketConsumer

from . import tasks


class ElectrocardiogramConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        electrocardiogram_id_json = json.loads(text_data)
        electrocardiogram_id = electrocardiogram_id_json.get('electrocardiogramId')
        expectation_and_dispersion_task = tasks.math_expectation_and_dispersion \
            .apply_async((electrocardiogram_id,), countdown=4)
        expectation_and_dispersion_results = expectation_and_dispersion_task.get()
        result_json = json.dumps(expectation_and_dispersion_results)
        self.send(text_data=result_json)
