# Custom Serializers

This repo provides several implementations of custom serializers in [Lingua Franca](lf-lang.org).

## Syntax

To use the custom serializer in a connection, the syntax is as follows:

```
<source_port_reference> -> <destination_port_reference> after <time_value> serializer "<serializer_name>"
```

The `<serializer_name>` can be any python package that exports a class `Serializer` that satisfies the following API:

```python-repl
class Serializer():
    def serialize(self, obj)->bytes:
        return <bytes_object>
    def deserialize(self, message:bytes):
        return <deserialized_object>
```

## Implementation

This repo provides several implementations.

* `pickle_serializer`: Default pickle serializer.
* `pickle5_serializer`: Serializes and deserializes with pickle version 5.
* `plasma_serializer`: zero-copy inter-process communication using [Plasma In-Memory Object Store](https://arrow.apache.org/docs/3.0/python/plasma.html).
* `shm_serializer`: shared memory inter-process communication.
* `transparent`: asserts the object being passed in the connection is a bytes object and transfer it as-is.

## Install

Install the desired `<serializer_name>` with command

```bash
pip install ./<serializer_name>/
```

## Compatability

This feature is backwards compatible. If `<serializer_name>` is any of `[NATIVE, ROS2, PROTO]`, it will use these serialization methods instead of finding a python package.
