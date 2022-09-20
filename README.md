# slobs_websocket

Python library to communicate with [Streamlabs OBS](https://streamlabs.com) Client.

_Licensed under the GPL v3 License_

## Project Pages

GitHub project: https://github.com/eumario/slobs_websocket

PyPI package: To be updated

## Installation

Just run `pip install git+https://github.com/eumario/slobs_websocket.git#egg=slobs_websocket` in your Python venv or directly on your system.

For manual installation, git clone the github repository and copy the directory **slobs_websocket** into your python project.

**Requires**: websocket-client (from pip), tomli

## Usage

See python scripts in the [samples](https://github.com/eumario/slobs_websocket/tree/master/samples) directory.

## Simple Example

Below is a simple example of getting the list of scenes in your current Scene collection, and printing out their name.

```python
from slobs_websocket import StreamlabsOBS

with StreamlabsOBS() as client:
    scenes = client.ScenesService.getScenes()

    for scene in scenes:
        print(scene.name)
```

## Design of Library

Inspiration for design of library comes from a Ruby background of meta programming, meaning that all calls in library goes through a base **BasicService** class, or **BasicEventService** class, for services that support events. These two classes implement the core of the work to be done in the library for each service class that Streamlabs provides.

When you initialize the **StreamlabsOBS** class, it will initialize all of the service classes for you automatically as accessors on the client object, making it easier to use dot notation to make your Websocket calls. No need for creating a request, and sending it, getting the response, and parsing the data. The library will automatically map data based upon the result, to the appropriate object classes.

Accessing the result data, is a simple as knowing what field the Json provides for each object. An example taken from the API Reference for Scenes:

```
{'_type': 'HELPER',
 'resourceId': 'Scene["scene_f50c15b3-c4c3-4798-be45-24091edefd0d"]',
 'id': 'scene_f50c15b3-c4c3-4798-be45-24091edefd0d',
 'name': 'Starting Soon',
 'nodes': [{'id': '25104d69-1f91-4bc2-8a11-391bf5e20fc7',
   'sceneId': 'scene_f50c15b3-c4c3-4798-be45-24091edefd0d',
   'sceneNodeType': 'item',
   'parentId': '',
   'sourceId': 'browser_source_80b03f26-3384-48bf-8f4e-73ae01f17bbf',
   'sceneItemId': '25104d69-1f91-4bc2-8a11-391bf5e20fc7',
   'name': 'Chat Box',
   'resourceId': 'SceneItem["scene_f50c15b3-c4c3-4798-be45-24091edefd0d", "25104d69-1f91-4bc2-8a11-391bf5e20fc7", "browser_source_80b03f26-3384-48bf-8f4e-73ae01f17bbf"]',
   'transform': {'position': {'x': 48.90566037735846, 'y': 45.99659284497443},
    'scale': {'x': 1, 'y': 1},
    'crop': {'top': 0, 'bottom': 0, 'left': 0, 'right': 0},
    'rotation': 0},
   'visible': True,
   'locked': False,
   'streamVisible': True,
   'recordingVisible': True},
  {'id': '3114934c-e33e-42b2-ab8f-01ca6f294575',
   'sceneId': 'scene_f50c15b3-c4c3-4798-be45-24091edefd0d',
   'sceneNodeType': 'item',
   'parentId': '',
   'sourceId': 'image_source_2047acd3-21a7-489c-8f9d-043ef1b93ba5',
   'sceneItemId': '3114934c-e33e-42b2-ab8f-01ca6f294575',
   'name': 'Overlay Starting Soon',
   'resourceId': 'SceneItem["scene_f50c15b3-c4c3-4798-be45-24091edefd0d", "3114934c-e33e-42b2-ab8f-01ca6f294575", "image_source_2047acd3-21a7-489c-8f9d-043ef1b93ba5"]',
   'transform': {'position': {'x': 0, 'y': 0},
    'scale': {'x': 1, 'y': 1},
    'crop': {'top': 0, 'bottom': 0, 'left': 0, 'right': 0},
    'rotation': 0},
   'visible': True,
   'locked': False,
   'streamVisible': True,
   'recordingVisible': True}]}
```

As you can see from the JSON Response above, the Scene object, will have accessors for resourceId, id, name and nodes, that you would access as: **scene.id**, **scene.name**, or even **scene.nodes** will return the array with the nodes. All Arrays with objects in them, will be converted to their proper format, EG: SceneNodeItem for Items, and such.

## Problems?

Please check on [Github project issues](https://github.com/eumario/slobs_websocket/issues), and if no one else has experienced the problem you are having, you can [file a new issue](https://github.com/eumario/slobs_websocket/issues/new).
