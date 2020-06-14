from .basic_service import BasicService

class SelectionService(BasicService):
    """
        Properties
    """

    sceneId: ""

    """
        Accessors
    """

    def selection(self):
        return self._send_packet()

    """
        Methods
    """

    def add(self,ids):
        return self._send_packet(ids)

    def centerOnScreen(self):
        return self._send_packet()
    
    def clone(self):
        return self._send_packet()

    def copyTo(self,sceneId, folderId=None, duplicateSources=False):
        return self._send_packet(sceneId, folderId, duplicateSources)

    def deselect(self,ids):
        return self._send_packet(ids)

    def fitToScreen(self):
        return self._send_packet()

    def flipX(self):
        return self._send_packet()

    def flipY(self):
        return self._send_packet()

    def getBoundingRect(self):
        return self._send_packet()

    def getFolders(self):
        return self._send_packet()

    def getIds(self):
        return self._send_packet()

    def getInverted(self):
        return self._send_packet()

    def getInvertedIds(self):
        return self._send_packet()

    def getItems(self):
        return self._send_packet()

    def getLastSelected(self):
        return self._send_packet()

    def getLastSelectedId(self):
        return self._send_packet()

    def getModel(self):
        return self._send_packet()

    def getRootNodes(self):
        return self._send_packet()

    def getScene(self):
        return self._send_packet()

    def getSize(self):
        return self._send_packet()

    def getSources(self):
        return self._send_packet()

    def getVisualItems(self):
        return self._send_packet()

    def invert(self):
        return self._send_packet()

    def isSelected(self):
        return self._send_packet()

    def moveTo(self, sceneId, folderId=None):
        return self._send_packet(sceneId, folderId)

    def placeAfter(self, sceneNodeId):
        return self._send_packet(sceneNodeId)

    def placeBefore(self, sceneNodeId):
        return self._send_packet(sceneNodeId)

    def remove(self):
        return self._send_packet()

    def reset(self):
        return self._send_packet()

    def resetTransform(self):
        return self._send_packet()

    def rotate(self):
        return self._send_packet()

    def scale(self, scale, origin=None):
        return self._send_packet(scale, origin)

    def scaleWithOffset(self, scale, offset):
        return self._send_packet(scale, offset)

    def select(self, ids):
        return self._send_packet(ids)

    def selectAll(self):
        return self._send_packet()

    def setContentCrop(self):
        return self._send_packet()

    def setParent(self, folderId):
        return self._send_packet(folderId)

    def setSettings(self, settings):
        return self._send_packet(settings)

    def setTransform(self, transform):
        return self._send_packet(transform)

    def setVisibility(self, visible):
        return self._send_packet(visible)

    def stretchToScreen(self):
        return self._send_packet()
