from .base_object import BaseObject
from slobs_websocket.util_funcs import Utils

class Scene(BaseObject):
    def addFile(self, path, folderId):
        return self._send_packet(path, folderId, resource=self.resourceId)

    def addSource(self, sourceId, options=None):
        return self._send_packet(sourceId, options, resource=self.resourceId)

    def canAddSource(self, sourceId):
        return self._send_packet(sourceId, resource=self.resourceId)

    def clear(self):
        return self._send_packet(resource=self.resourceId)

    def createAndAddSource(self, name, type):
        return self._send_packet(name, type, resource=self.resourceId)

    def createFolder(self, name):
        return self._send_packet(name, resource=self.resourceId)

    def getFolder(self, sceneFolderId):
        return Utils.toSceneItemFolder(self._send_packet(sceneFolderId, resource=self.resourceId))

    def getFolders(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getItem(self, sceneItemID):
        return Utils.parseNodes([self._send_packet(sceneItemID, resource=self.resourceId)])[0]

    def getItems(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getModel(self):
        return self._send_packet(resource=self.resourceId)

    def getNestedItems(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getNestedScenes(self):
        return Utils.parseScenes(self._send_packet(resource=self.resourceId))

    def getNestedSources(self):
        return Utils.parseSources(self._send_packet(resource=self.resourceId))

    def getNode(self, sceneNodeId):
        return Utils.parseNodes([self._send_packet(sceneNodeId, resource=self.resourceId)])[0]

    def getNodeByName(self, name):
        return Utils.parseNodes([self._send_packet(name, resource=self.resourceId)])[0]

    def getNodes(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getRootNodes(self):
        return Utils.parseNodes(elf._send_packet(resource=self.resourceId))

    def getSelection(self, ids):
        return self._send_packet(ids, resource=self.resourceId)

    def getSource(self):
        return Utils.toSource(self._send_packet(resource=self.resourceId))

    def makeActive(self):
        return self._send_packet(resource=self.resourceId)

    def remove(self):
        return self._send_packet(resource=self.resourceId)

    def removeFolder(self, folderId):
        return self._send_packet(folderId, resource=self.resourceId)

    def removeItem(self, sceneItemId):
        return self._send_packet(sceneItemId, resource=self.resourceId)

    def setName(self, newName):
        return self._send_packet(newName, resource=self.resourceId)
