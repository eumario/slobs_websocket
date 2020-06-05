import websocket
import threading
import logging
import json
from slobs_websocket import exceptions

class RecvThread(threading.Thread):

    def __init__(self, core, log, debugJson=False):
        self.core = core
        self.ws = core.ws
        self.running = True
        self.log = log
        self.debugJson = debugJson
        self.events = {}
        threading.Thread.__init__(self)

    def run(self):
        while self.running:
            message = ""
            try:
                message = self.ws.recv()

                # recv() can return an empty string
                if not message:
                    continue

                result = json.loads(message)

                if self.debugJson:
                    self.log.debug(u"Payload Dump: {}".format(result))

                if 'error' in result:
                    if self.debugJson:
                        self.log.error(u"Got error message: {}".format(result))
                    if 'id' in result and not result["id"] == None:
                        id, data = (result["id"], result["error"])
                        data["error"] = True
                        self.core.packets[id] = data
                elif 'id' in result and not result["id"] == None:
                    id, data = (result['id'], result['result'])
                    self.log.info(u"Got Result for id: {}".format(id))
                    self.core.packets[id] = data
                elif '_type' in result['result'] and result['result']['_type'] == "EVENT":
                    result = result["result"]
                    data = result.pop("data")
                    event = result["resourceId"]
                    self.log.debug(u"Got Event: {}".format(event))
                    if event in self.events:
                        self.events[event]._processEvent(event.split(".")[1],data)
                    else:
                        raise exceptions.EventError("Event {} not subscribed to yet!".format(event))
                else:
                    self.log.error(u"Unknown message: {}".format(result))
            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    self.core.reconnect()
            except OSError as e:
                if self.running:
                    raise e
            except (ValueError, exceptions.ObjectError) as e:
                self.log.error(u"Invalid message: {} ({})".format(message, e))
        self.log.debug("RecvThread ended.")
