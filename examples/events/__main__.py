import time

from slobs_websocket import StreamlabsOBS


def on_scene_switched(data):
    print(f"Switched to scene {data.name}")


def on_source_added(data):
    print(f"Added source {data.id}")


def on_source_removed(data):
    print(f"Removed source {data.name}")


def main():
    with StreamlabsOBS() as client:
        client.ScenesService.sceneSwitched += on_scene_switched
        client.SourcesService.sourceAdded += on_source_added
        client.SourcesService.sourceRemoved += on_source_removed

        time.sleep(30)


if __name__ == "__main__":
    main()
