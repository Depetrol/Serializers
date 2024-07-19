import pickle

class Serializer():
    def serialize(self, obj)->bytes:
        return pickle.dumps(obj, protocol=5)
    def deserialize(self, message:bytes):
        return pickle.loads(message)