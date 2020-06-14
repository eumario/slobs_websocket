from .basic_service import BasicService

class NotificationsService(BasicService):
    def applyAction(self,notificationId):
        return self._send_packet(notificationId)

    def getAll(self,type):
        return self._send_packet(type)

    def getNotification(self,id):
        return self._send_packet(id)

    def getRead(self,type):
        return self._send_packet(type)

    def getSettings(self):
        return self._send_packet()

    def getUnread(self,type):
        return self._send_packet(type)

    def markAllAsRead(self):
        return self._send_packet()

    def markAsRead(self,id):
        return self._send_packet(id)

    def push(self,notifyInfo):
        return self._send_packet(notifyInfo)

    def restoreDefaultSettings(self):
        return self._send_packet()

    def setSettings(self,patch):
        return self._send_packet(patch)

    def showNotifications(self):
        return self._send_packet()
