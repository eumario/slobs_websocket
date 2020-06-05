from .basic_event_service import BasicEventService

class SourcesService(BasicEventService):
    """
        Events
    """
    __events__ = ["sourceAdded","sourceRemoved","sourceUpdated"]

    """
        Methods
    """

    def addFile(self, path):
        return self._send_packet(path)

    def createSource(self, name, type, settings=None, options=None):
        return self._send_packet(name,type,settings,options)

    def getAvailableSourcesTypeList(self):
        return self._send_packet()

    def getSource(self, sourceId):
        return self._send_packet(sourceId)

    def getSources(self):
        return self._send_packet()

    def getSourcesByName(self, name):
        return self._send_packet(name)

    def removeSource(self, id):
        return self._send_packet(id)

    def showAddSource(self, sourceType):
        return self._send_packet(sourceType)

    def showShowcase(self):
        return self._send_packet()

    def showSourceProperties(self, sourceId):
        return self._send_packet(sourceId)
