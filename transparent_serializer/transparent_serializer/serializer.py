import pickle


class Serializer:
    def serialize(self, obj) -> bytes:
        assert isinstance(obj, bytes)
        return obj

    def deserialize(self, message: bytes):
        return message
