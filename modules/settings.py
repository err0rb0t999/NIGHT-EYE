from rich.console import Console
from rich.table import Table

from utils.config import load_config, save_config

console = Console()


def settings_menu():

    while True:

        config = load_config()

        table = Table(title="Settings")

        table.add_column("Option", style="cyan")
        table.add_column("Current", style="green")

        table.add_row("1. Theme", config["theme"])
        table.add_row("2. Save JSON", str(config["save_json"]))
        table.add_row("3. Save HTML", str(config["save_html"]))
        table.add_row("4. Check Internet", str(config["check_internet"]))
        table.add_row("5. Show Banner", str(config["show_banner"]))
        table.add_row("0. Back", "")

        console.print(table)

        choice = input("\nSelect > ")

        if choice == "1":
            config["theme"] = input("Theme Name: ").strip() or "default"

        elif choice == "2":
            config["save_json"] = not config["save_json"]

        elif choice == "3":
            config["save_html"] = not config["save_html"]

        elif choice == "4":
            config["check_internet"] = not config["check_internet"]

        elif choice == "5":
            config["show_banner"] = not config["show_banner"]

        elif choice == "0":
            save_config(config)
            return

        else:
            console.print("[red]Invalid choice[/red]")
            continue

        save_config(config)
        console.print("[green]Settings updated.[/green]")
