"""
    Central API
"""

import json
import inspect
import websocket
import logging
import time
import socket

from .services import *
from . import exceptions
from .recv_thread import RecvThread
from .service_connection import ServiceConnection

class StreamlabsOBS():
    """
        Core class for StreamlabsOBS Client.  This creates, and manages the
        websocket to use for connecting to Streamlabs OBS, as well as
        dispatching, and receiving messages.

        Simple Usage:
        >>> from slobs_websocket import StreamlabsOBS
        >>> client = StreamlabsOBS("/api",host="localhost",port=59650)
        >>> client.connect()
        >>> client.ScenesService.getScenes()
        [
            {
                "_type": "HELPER",
                "resourceId": "Scene[\"3efd436e5546\"]",
                "id": "3efd436e5546",
                "name": "My super scene",
                "activeItemIds": []
            },
            {
                "_type": "HELPER",
                "resourceId": "Scene[\"6b615869aba3\"]",
                "id": "6b615869aba3",
                "name": "New Scene",
                "activeItemIds": []
            }
        ]
        >>> client.disconnect()
    """

    def __init__(self, prefix="/api", host="localhost", port=59650, debug=False, debugJson=False):
        """
        Construct a new StreamlabsOBS Client

        :param prefix: Prefix in which to access the API (Default is '/api')
        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 59650)
        :param debug: debug logs for connections.
        """

        # Connection information
        self.prefix = prefix
        self.host = host
        self.port = port
        self.thread_recv = None
        self.nextId = 0
        self.packets = {}
        self.log = logging.getLogger(__name__)
        ch = logging.StreamHandler()
        self.log.addHandler(ch)

        # For debugging
        self.debug = debug
        if self.debug:
            self.log.setLevel(logging.DEBUG)
            ch.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.INFO)
            ch.setLevel(logging.INFO)

        self.debugJson = debugJson

        # Websocket URL to connect to
        self.url = "ws://{}:{}{}/websocket".format(self.host,self.port,self.prefix)
        self.log.debug("Websocket URL: {}".format(self.url))

        ServiceConnection(self,self.log)
        # Services in which is used with slobs.
        self.AudioService = AudioService()
        self.NotificationsService = NotificationsService()
        self.SceneCollectionsService = SceneCollectionsService()
        self.ScenesService = ScenesService()
        self.SelectionService = SelectionService()
        self.SourcesService = SourcesService()
        self.StreamingService = StreamingService()

    def connect(self, host=None, port=None):
        """
        Connect to the websocket server

        :return: Nothing
        """
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

        if host is not None or port is not None:
            self.url = "ws://{}:{}{}/websocket".format(self.host, self.port, self.prefix)
            self.log.debug("Websocket URL: {}".format(self.url))

        try:
            self.ws = websocket.WebSocket()
            self.log.info("Connecting...")
            self.ws.connect(self.url)
            self.log.info("Connected!")
            self._run_threads()
        except socket.error as e:
            raise exceptions.ConnectionFailure(str(e))

    def _run_threads(self):
        if self.thread_recv is not None:
            self.thread_recv.running = False
        self.thread_recv = RecvThread(self, self.log, debugJson = self.debugJson)
        self.thread_recv.daemon = True
        self.thread_recv.start()

    def reconnect(self):
        """
        Restarts the connection to the websocket server

        :return: Nothing
        """
        try:
            self.disconnect()
        except Exception:
            # TODO: Need to catch more percise exception
            pass
        self.connect()

    def disconnect(self):
        """
        Disconnect from websocket server

        :return: Nothing
        """
        self.log.info("Disconnecting...")
        if self.thread_recv is not None:
            self.thread_recv.running = False

        try:
            self.ws.close()
        except socket.error:
            pass

        if self.thread_recv is not None:
            self.thread_recv.join()
            self.thread_recv = None

    def _send_packet(self, *args, **kwargs):
        self.nextId += 1
        frm  = inspect.stack()[1]
        cls = frm[0].f_locals.get('self',None)
        method = frm.function
        if cls == None:
            resource = ""
        else:
            resource = cls.__class__.__name__

        if "method" in kwargs:
            method = kwargs["method"]

        if "resource" in kwargs:
            resource = kwargs["resource"]

        # Initial Payload
        payload = {
            "jsonrpc": "2.0",
            "id": self.nextId,
            "method": method,
            "params": {}
        }

        # Inject into payload any Keyword Arguments
        for key, value in kwargs.items():
            if key == "method":
                continue
            payload["params"][key] = value

        # Now check to see if we have a resource in our params:
        if not "resource" in payload["params"]:
            # We don't have a resource, so we should provide one (Provided by Services listed above)
            payload["params"]["resource"] = resource

        # Finally, we add the non keyword arguments to our payload
        payload["params"]["args"] = list(args)
        if self.debugJson:
            self.log.debug("Payload JSON: {}".format(payload))

        self.ws.send(json.dumps(payload))
        return self._wait_message(self.nextId)

    def _wait_message(self, message_id):
        timeout = time.time() + 60 # Timeout = 60s
        while time.time() < timeout:
            if message_id in self.packets:
                packet = self.packets.pop(message_id)
                if "error" in packet:
                    raise exceptions.ObjectError(u"Error({}) - {}".format(packet['code'], packet['message'].split("\n")[0]))
                else:
                    return packet
            time.sleep(0.1)
        raise exceptions.MessageTimeout(u"No answer for message {}".format(message_id))