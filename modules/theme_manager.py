import json

from rich.console import Console
from rich.table import Table

from utils.theme import available_themes

console = Console()


def theme_manager():

    with open("config/settings.json", "r") as f:
        settings = json.load(f)

    themes = available_themes()

    table = Table(title="Theme Manager")

    table.add_column("ID", style="cyan")
    table.add_column("Theme", style="green")

    for i, t in enumerate(themes, start=1):
        table.add_row(str(i), t)

    console.print(table)

    choice = input("\nSelect Theme > ")

    try:

        theme = themes[int(choice)-1]

        settings["theme"] = theme

        with open("config/settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        console.print(
            f"\n[green]Theme changed to {theme}[/green]"
        )

    except Exception:

        console.print("[red]Invalid Choice[/red]")
