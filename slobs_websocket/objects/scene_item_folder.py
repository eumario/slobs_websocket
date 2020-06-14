from slobs_websocket.util_funcs import Utils
from .scene_node import SceneNode

class SceneItemFolder(SceneNode):
    def add(self,sceneNodeId):
        return self._send_packet(sceneNodeId, resource=self.resourceId)

    def getFolders(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getItems(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def getNestedNodes(self):
        return Utils.parseNodes(self._send_packet(resource=self.resourceId))

    def ungroup(self):
        return self._send_packet(resource=self.resourceId)