from .scene_node import SceneNode
from slobs_websocket.util_funcs import Utils

class SceneItem(SceneNode):
    def centerOnScreen(self):
        return self._send_packet(resource=self.resourceId)

    def fitToScreen(self):
        return self._send_packet(resource=self.resourceId)

    def flipX(self):
        return self._send_packet(resource=self.resourceId)

    def flipY(self):
        return self._send_packet(resource=self.resourceId)

    def getSource(self):
        return Utils.toSource(self._send_packet(resource=self.resourceId))

    def resetTransform(self):
        return self._send_packet(resource=self.resourceId)

    def rotate(self, deg):
        return self._send_packet(deg, resource=self.resourceId)

    def setContentCrop(self):
        return self._send_packet(resource=self.resourceId)

    def setScale(self, newScaleModel, origin = None):
        return self._send_packet(newScaleModel, origin, resource=self.resourceId)

    def setSettings(self, settings):
        return self._send_packet(settings, resource=self.resourceId)

    def setTransform(self, transform):
        return self._send_packet(transform, resource=self.resourceId)

    def setVisibility(self, visible):
        return self._send_packet(visible, resource=self.resourceId)

    def stretchToScreen(self):
        return self._send_packet(resource=self.resourceId)