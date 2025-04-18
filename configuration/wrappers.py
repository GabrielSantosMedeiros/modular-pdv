import json


def Singleton(cls):
    _instances = {}
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper


def JsonSerializer(cls):
    def __json__(self, *args, **kwargs):
        attrs = {key: str(value) for key, value in self.__data__.items()}
        return json.dumps(attrs, indent=4)
    cls.__json__ = __json__
    return cls