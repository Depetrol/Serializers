import pickle
from multiprocessing import shared_memory

class Serializer():
    def serialize(self, data):
        serialized_array = pickle.dumps(data)
        ob_size = len(serialized_array)
        local_shm = shared_memory.SharedMemory(create=True, size=ob_size)
        local_shm.buf[:ob_size] = serialized_array
        return pickle.dumps(local_shm.name, ob_size)
    def deserialize(self, obj):
        ob_name, ob_size = pickle.loads(obj)
        local_shm = shared_memory.SharedMemory(name=ob_name)
        data = pickle.loads(local_shm.buf[:ob_size])
        local_shm.close()
        local_shm.unlink()
        return data