import json
from pathlib import Path

THEMES_FILE = Path("config/themes.json")
SETTINGS_FILE = Path("config/settings.json")


def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_theme():

    themes = _load_json(THEMES_FILE)

    settings = _load_json(SETTINGS_FILE)

    name = settings.get("theme", "default")

    return themes.get(name, themes["default"])


def available_themes():

    return list(_load_json(THEMES_FILE).keys())
