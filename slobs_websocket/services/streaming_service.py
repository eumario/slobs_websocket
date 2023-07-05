from .basic_event_service import BasicEventService

class StreamingService(BasicEventService):
    """
        Events
    """
    __events__ = ["streamingStatusChange"]

    """
        Methods
    """
    def getModel(self):
        return self._send_packet()

    def saveReplay(self):
        return self._send_packet()

    def startReplayBuffer(self):
        return self._send_packet()

    def stopReplayBuffer(self):
        return self._send_packet()

    def toggleRecording(self):
        return self._send_packet()

    def toggleStreaming(self):
        return self._send_packet()
