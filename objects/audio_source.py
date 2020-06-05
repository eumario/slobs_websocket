from .base_object import BaseObject

class AudioSource(BaseObject):
    def getModel(self):
        return self._send_packet(resource = self.resourceId)

    def setDeflection(self,deflection):
        return self._send_packet(deflection, resource = self.resourceId)
    
    def setMuted(self,muted):
        return self._send_packet(muted, resource = self.resourceId)
