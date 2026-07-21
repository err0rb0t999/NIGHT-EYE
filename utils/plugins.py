from pathlib import Path


def get_plugins():

    plugin_dir = Path("modules")

    plugins = []

    for file in plugin_dir.glob("*.py"):

        if file.name.startswith("_"):
            continue

        if file.stem == "settings":
            continue

        plugins.append(file.stem)

    return sorted(plugins)
