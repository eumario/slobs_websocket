from .base_object import BaseObject
from slobs_websocket.util_funcs import Utils

class Source(BaseObject):

    def duplicate(self):
        return Utils.toSource(self._send_packet(resource=self.resourceId))

    def getModel(self):
        return self._send_packet(resource=self.resourceId)

    def getPropertiesFormData(self):
        return self._send_packet(resource=self.resourceId)

    def getSettings(self):
        return self._send_packet(resource=self.resourceId)

    def hasProps(self):
        return self._send_packet(resource=self.resourceId)

    def refresh(self):
        return self._send_packet(resource=self.resourceId)

    def setName(self, newName):
        return self._send_packet(newName, resource=self.resourceId)

    def setPropertiesFormData(self, properties):
        return self._send_packet(properties, resource=self.resourceId)

    def updateSettings(self, settings):
        return self._send_packet(resource=self.resourceId)
