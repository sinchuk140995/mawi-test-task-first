from django.utils import timezone

import mongoengine


# class Signal(mongoengine.EmbeddedDocument):
class Signal(mongoengine.Document):
    value = mongoengine.IntField(required=True)


class Electrocardiogram(mongoengine.Document):
    first_name = mongoengine.StringField(max_length=50, required=True)
    last_name = mongoengine.StringField(max_length=50, required=True)
    # signals = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Signal))
    signals = mongoengine.ListField(mongoengine.ReferenceField(Signal, dbref=False))
    start_date = mongoengine.DateTimeField(default=timezone.now)
    end_date = mongoengine.DateTimeField()
