
# Object Core Representation


class Utils():
    @classmethod
    def toAudioSource(cls,data: dict):
        from .objects.audio_source import AudioSource
        return AudioSource(data)

    @classmethod
    def toScene(cls, data: dict):
        from .objects.scene import Scene
        return Scene(data)

    @classmethod
    def toSceneItem(cls, data: dict):
        from .objects.scene_item import SceneItem
        return SceneItem(data)

    @classmethod
    def toSceneItemFolder(cls, data: dict):
        from .objects.scene_item_folder import SceneItemFolder
        return SceneItemFolder(data)

    @classmethod
    def toSceneNode(cls, data: dict):
        from .objects.scene_node import SceneNode
        return SceneNode(data)

    @classmethod
    def toSelection(cls, data: dict):
        from .objects.selection import Selection
        return Selection(data)

    @classmethod
    def toSource(cls, data: dict):
        from .objects.source import Source
        return Source(data)

    @classmethod
    def parseScenes(cls, data: list):
        nlist = []
        for scene in data:
            x = Utils.toScene(scene)
            x.nodes = Utils.parseNodes(x.nodes)
            nlist.append(x)
        return nlist

    @classmethod
    def parseNodes(cls, data: list):
        nlist = []
        for node in data:
            x = None
            if node["sceneNodeType"] == "item":
                x = Utils.toSceneItem(node)
            elif node["sceneNodeType"] == "folder":
                x = Utils.toSceneItemFolder(node)
            else:
                x = Utils.toSceneNode(node)
            nlist.append(x)
        return nlist

    @classmethod
    def parseAudioSources(cls, data: list):
        nlist = []
        for audio_source in data:
            nlist.append(Utils.toAudioSource(audio_source))
        return nlist

    @classmethod
    def parseSources(cls, data: list):
        nlist = []
        for source in data:
            nlist.append(Utils.toSource(source))
        return nlist
