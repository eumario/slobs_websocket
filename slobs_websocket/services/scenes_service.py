from .basic_event_service import BasicEventService
from slobs_websocket.util_funcs import Utils
from slobs_websocket.converter import *

class ScenesService(BasicEventService):
    """
        Events
    """
    __events__ = ["itemAdded","itemRemoved","itemUpdated","sceneAdded","sceneRemoved","sceneSwitched"]

    """
        Event Converters
    """

    @converter(["itemAdded","itemRemoved","itemUpdated"])
    def convertItem(data):
        return Utils.toSceneItem(data)

    @converter(["sceneAdded","sceneRemoved","sceneSwitched"])
    def convertScene(data):
        return Utils.toScene(data)

    """
        Accessors
    """
    def activeScene(self):
        return Utils.toScene(self._send_packet())

    def activeSceneId(self):
        return self._send_packet()

    """
        Methods
    """

    def createScene(self,name):
        return Utils.toScene(self._send_packet(name))

    def getScene(self,id):
        return Utils.toScene(self._send_packet(id))

    def getScenes(self):
        return Utils.parseScenes(self._send_packet())

    def makeSceneActive(self,id):
        return self._send_packet(id)

    def removeScene(self,id):
        return self._send_packet(id)