#!/usr/bin/env python3

import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from banner import banner
from config.settings import VERSION

from utils.loader import loading
from utils.network import internet_available
from utils.helpers import check_dependencies, quit_program
from utils.logger import info, error
from modules.theme_manager import theme_manager

from modules.ip_lookup import ip_lookup
from modules.domain_lookup import domain_lookup
from modules.phone_parser import phone_parser
from modules.settings import settings_menu
from modules.dashboard import dashboard

console = Console()


def clear():
    os.system("clear")


def startup():
    loading("Starting TS-OSINT Pro...", 2)

    missing = check_dependencies()

    if missing:
        console.print(
            Panel(
                "\n".join(missing),
                title="Missing Python Modules",
                border_style="red"
            )
        )
        console.print(
            "\nRun:\n"
            "[bold cyan]pip install -r requirements.txt[/bold cyan]\n"
        )
        quit_program()

    if internet_available():
        console.print("[bold green]✔ Internet Connected[/bold green]")
        info("Internet Connected")
    else:
        console.print("[bold yellow]⚠ No Internet Connection[/bold yellow]")
        error("No Internet Connection")

    info("TS-OSINT Started")


def menu():

    table = Table(
        title=f"TS-OSINT PRO v{VERSION}",
        show_lines=True
    )

    table.add_column("ID", justify="center", style="cyan", width=8)
    table.add_column("Module", style="green")
   
    table.add_row("01", "Phone Parser")
    table.add_row("02", "Email Parser")
    table.add_row("03", "Username Search")
    table.add_row("04", "Domain Lookup")
    table.add_row("05", "IP Lookup")
    table.add_row("06", "Metadata")
    table.add_row("07", "Reports")
    table.add_row("08", "Settings")
    table.add_row("09", "Plugins")
    table.add_row("10", "Dashboard")
    table.add_row("00", "Exit")
    table.add_row("12", "Theme Manager")
    console.print(table)


def wait():
    input("\nPress Enter to continue...")


def redraw():
    clear()
    banner()


def main():

    clear()

    banner()

    startup()

    while True:

        menu()

        choice = input("\nSelect Option > ").strip()

        if choice == "01":

            info("Phone Parser Selected")

            phone_parser()

            wait()
            redraw()
        elif choice == "04":

            domain_lookup()

            wait()

            redraw()

        elif choice == "05":

            ip_lookup()

            wait()

            redraw()

        elif choice == "12":

            theme_manager()

            wait()

            redraw()

        elif choice == "08":

            info("Settings Opened")

            settings_menu()

            wait()

            redraw()

        elif choice == "10":

            info("Dashboard Opened")

            dashboard()

            wait()

            redraw()

        elif choice == "00":

            info("Application Closed")

            quit_program()

        else:

            console.print(
                "[bold yellow]Module Coming Soon...[/bold yellow]"
            )

            wait()

            redraw()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]Interrupted by User[/bold red]")
        info("Interrupted by User")
    except Exception as e:
        error(str(e))
        console.print(f"\n[bold red]Fatal Error:[/bold red] {e}")
