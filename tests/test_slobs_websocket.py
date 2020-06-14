import sys
import os
sys.path.insert(0,os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")))

from slobs_websocket import StreamlabsOBS
import time

def printf(msg,*args):
	print(msg.format(*args), end="")

def puts(msg,*args):
	print(msg.format(*args))

client = StreamlabsOBS(debug=True, debugJson=True, apikey="156d3ebfd1538520fcded2547856d2bf9db6fb58")
client.connect(host="192.168.0.56")

client.SceneCollectionsService.collectionAdded += lambda x: printf("Collection Added: {}\n> ",x)
client.SceneCollectionsService.collectionRemoved += lambda x: printf("Collection Removed: {}\n> ",x)
client.SceneCollectionsService.collectionSwitched += lambda x: printf("Collection Switched: {}\n> ",x)
client.SceneCollectionsService.collectionUpdated += lambda x: printf("Collection Updated: {}\n> ",x)
client.SceneCollectionsService.collectionWillSwitch += lambda x: printf("Collection Will Switch: {}\n> ",x)

while True:
	res = input("> ")
	if res == "quit" or res == "exit":
		break
	time.sleep(0.1)
