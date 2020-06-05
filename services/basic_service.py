from slobs_websocket.service_connection import ServiceConnection

class BasicService():
    def __getattr__(self, name):
        return getattr(ServiceConnection,name)