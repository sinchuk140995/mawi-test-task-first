import mongoengine


class Signal(mongoengine.EmbeddedDocument):
    value = mongoengine.IntField(required=True)


class Electrocardiogram(mongoengine.Document):
    first_name = mongoengine.StringField(max_length=50, required=True)
    last_name = mongoengine.StringField(max_length=50, required=True)
    signals = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Signal))
