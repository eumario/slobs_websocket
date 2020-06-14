from .basic_service import BasicService
from slobs_websocket.util_funcs import Utils

class AudioService(BasicService):
    def getSource(self,sourceId):
        return AudioSource(self._send_packet(sourceId))

    def getSources(self):
        return Utils.parseAudioSources(self._send_packet())

    def getSourcesForCurrentScene(self):
        return Utils.parseAudioSources(self._send_packet())

    def getSourcesForScene(self,sceneId):
        return Utils.parseAudioSources(self._send_packet(sceneId))
