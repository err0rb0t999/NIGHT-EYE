from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()


def banner():

    logo = Text("""
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ███████╗██╗   ██╗███████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔════╝╚██╗ ██╔╝██╔════╝
██╔██╗ ██║██║██║  ███╗███████║   ██║       █████╗   ╚████╔╝ █████╗
██║╚██╗██║██║██║   ██║██╔══██║   ██║       ██╔══╝    ╚██╔╝  ██╔══╝
██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ███████╗   ██║   ███████╗
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝   ╚═╝   ╚══════╝
""", style="bold bright_cyan")

    console.print(
        Panel(
            Align.center(logo),
            title="[bold bright_cyan]👁 NIGHT-EYE[/bold bright_cyan]",
            subtitle="[bold yellow]Engineered by M00N[/bold yellow]",
            border_style="bright_cyan",
            padding=(1, 2)
        )
    )

    console.print(
        Align.center(
            "[bold bright_white]👁 NIGHT-EYE[/bold bright_white]"
        )
    )

    console.print(
        Align.center(
            "[bold bright_cyan]Professional Digital Intelligence & OSINT Framework[/bold bright_cyan]"
        )
    )

    console.print(
        Align.center(
            "[bright_white]Version 6.0.0[/bright_white] • "
            "[bright_magenta]Python 3[/bright_magenta] • "
            "[bright_yellow]Rich UI[/bright_yellow]"
        )
    )

    console.rule("[bold bright_cyan]Developed by M00N[/bold bright_cyan]")
