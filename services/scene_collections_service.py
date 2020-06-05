from .basic_event_service import BasicEventService

class SceneCollectionsService(BasicEventService):
    
    """
        Events
    """
    __events__ = ["collectionAdded", "collectionRemoved", "collectionSwitched", "collectionUpdated", "collectionWillSwitch"]
    
    """
        Accessors
    """
    def activeCollection(self):
        return self._send_packet()

    def collections(self):
        return self._send_packet()

    """
        Methods
    """


    def create(self,options):
        return self._send_packet(options)

    def fetchSceneCollectionsSchema(self):
        return self._send_packet()

    def load(self,id):
        return self._send_packet(id)

    def rename(self, newName, id):
        return self._send_packet(newName, id)
