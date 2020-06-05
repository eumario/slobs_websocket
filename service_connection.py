class SCMetaClass(type):
    def __getattr__(cls,name):
        try:
            return getattr(ServiceConnection.instance.conn,name)
        except AttributeError:
            return getattr(ServiceConnection.instance.log,name)

class ServiceConnection(metaclass=SCMetaClass):

    class __ServiceConnection():
        def __init__(self, connection, log):
            self.conn = connection
            self.log = log
    instance = None

    def __init__(self, connection, log):
        if not ServiceConnection.instance:
            ServiceConnection.instance = ServiceConnection.__ServiceConnection(connection,log)
        else:
            ServiceConnection.instance.conn = connection
            ServiceConnection.instance.log = log