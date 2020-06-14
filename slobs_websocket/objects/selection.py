from .base_object import BaseObject
from slobs_websocket.util_funcs import Utils

class Selection(BaseObject):
    def add(self, ids):
        return Utils.toSelection(self._send_packet(ids, resource=self.resourceId))

    def centerOnScreen(self):
        return self._send_packet(resource=self.resourceId)

    def clone(self):
        return Utils.toSelection(self._send_packet(resource=self.resourceId))

    def copyTo(self, sceneId, folderId = None, duplicateSources = False):
        return self._send_packet(sceneId, folderId, duplicateSources, resource=self.resourceId)

    def deselect(self,ids):
        return Utils.toSelection(self._send_packet(ids, resource=self.resourceId))

    def fitToScreen(self):
        return self._send_packet(resource=self.resourceId)

    def flipX(self):
        return self._send_packet(resource=self.resourceId)

    def flipY(self):
        return self._send_packet(resource=self.resourceId)

    def getBoundingRect(self):
        return self._send_packet(resource=self.resourceId)

    def getFolders(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getIds(self):
        return self._send_packet(resource=self.resourceId)

    def getInverted(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getInvertedIds(self):
        return self._send_packet(resource=self.resourceId)

    def getItems(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getLastSelected(self):
        return Utils.parseNodes([self._send_packet(resource=self.resourceId)])[0]

    def getLastSelectedId(self):
        return self._send_packet(resource=self.resourceId)

    def getModel(self):
        return self._send_packet(resource=self.resourceId)

    def getRootNodes(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getScene(self):
        return Utils.toScene(self._send_packet(resource=self.resourceId))

    def getSize(self):
        return self._send_packet(resource=self.resourceId)

    def getSources(self):
        return Utils.parseSources(self._send_packet(resource=self.resourceId))

    def getVisualItems(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def invert(self):
        return Utils.toSelection(self._send_packet(resource=self.resourceId))

    def isSceneFolder(self):
        return self._send_packet(resource=self.resourceId)

    def isSceneItem(self):
        return self._send_packet(resource=self.resourceId)

    def isSelected(self, nodeId):
        return self._send_packet(nodeId,resource=self.resourceId)

    def placeAfter(self, sceneNodeId):
        return self._send_packet(sceneNodeId, resource=self.resourceId)

    def placeBefore(self, sceneNodeId):
        return self._send_packet(sceneNodeId, resource=self.resourceId)

    def remove(self):
        return self._send_packet(resource=self.resourceId)

    def reset(self):
        return Utils.toSelection(self._send_packet(resource=self.resourceId))

    def resetTransform(self):
        return self._send_packet(resource=self.resourceId)

    def rotate(self, deg):
        return self._send_packet(deg, resource=self.resourceId)

    def scale(self, scale, origin=None):
        return self._send_packet(scale, origin, resource=self.resourceId)

    def scaleWithOffset(self, scale, offset):
        return self._send_packet(scale, offset, resource=self.resourceId)

    def select(self, ids):
        return Utils.toSelection(self._send_packet(ids, resource=self.resourceId))

    def selectAll(self):
        return Utils.toSelection(self._send_packet(resource=self.resourceId))

    def setContentCrop(self):
        return self._send_packet(resource=self.resourceId)

    def setParent(self, folderId):
        return self._send_packet(folderId, resource=self.resourceId)

    def setSettings(self, settings):
        return self._send_packet(settings, resource=self.resourceId)

    def setTransform(self, transform):
        return self._send_packet(transform, resource=self.resourceId)

    def setVisibility(self, visible):
        return self._send_packet(visible, resource=self.resourceId)

    def stretchToScreen(self):
        return self._send_packet(resource=self.resourceId)