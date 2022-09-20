from slobs_websocket import StreamlabsOBS


def main():
    # read conn info from config.toml
    with StreamlabsOBS() as client:
        scenes = client.ScenesService.getScenes()

        for scene in scenes:
            print(scene.name)


if __name__ == "__main__":
    main()
