import time

from slobs_websocket import StreamlabsOBS


def main():
    # read conn info from config.toml
    with StreamlabsOBS() as client:
        scenes = client.ScenesService.getScenes()

        for scene in scenes:
            print(f"Switching to scene {scene.name}")
            client.ScenesService.makeSceneActive(scene.id)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
