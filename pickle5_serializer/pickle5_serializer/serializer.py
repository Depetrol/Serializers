import pickle

class Serializer():
    def serialize(self, obj)->bytes:
        return pickle.dumps(self.serialize_one(obj), protocol=5)
    def deserialize(self, obj:bytes):
        return self.deserialize_one(pickle.loads(obj))