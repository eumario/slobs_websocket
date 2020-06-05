from .base_object import BaseObject
from slobs_websocket.util_funcs import Utils

class SceneNode(BaseObject):
    def addToSelection(self):
        return self._send_packet(resource=self.resourceId)

    def deselect(self):
        return self._send_packet(resource=self.resourceId)

    def detachParent(self):
        return self._send_packet(resource=self.resourceId)

    def getItemIndex(self):
        return self._send_packet(resource=self.resourceId)

    def getModel(self):
        return self._send_packet(resource=self.resourceId)

    def getNextItem(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getNextNode(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getNodeIndex(self):
        return self._send_packet(resource=self.resourceId)

    def getParent(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getPath(self):
        return self._send_packet(resource=self.resourceId)

    def getPrevItem(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getPrevNode(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getScene(self):
        return Utils.toScene(self._send_packet(resource=self.resourceId))

    def hasParent(self):
        return self._send_packet(resource=self.resourceId)

    def isFolder(self):
        return self._send_packet(resource=self.resourceId)

    def isItem(self):
        return self._send_packet(resource=self.resourceId)

    def isSelected(self):
        return self._send_packet(resource=self.resourceId)

    def placeAfter(self, nodeId):
        return self._send_packet(nodeId, resource=self.resourceId)

    def placeBefore(self, nodeId):
        return self._send_packet(nodeId, resource=self.resourceId)

    def remove(self):
        return self._send_packet(resource=self.resourceId)

    def select(self):
        return self._send_packet(resource=self.resourceId)

    def setParent(self, parentId):
        return self._send_packet(parentId, resource=self.resourceId)