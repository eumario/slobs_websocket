from slobs_websocket.service_connection import ServiceConnection

class BaseObject():
    def __init__(self, object):
        self.object = object

    def __getattr__(self, name):
        if name in self.object:
            return self.object[name]
        else:
            try:
                return getattr(ServiceConnection,name)
            except AttributeError:
                raise AttributeError("type object '{}' has no attribute '{}'".format(self.__class__.__name__, name))

