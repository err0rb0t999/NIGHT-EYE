from rich.console import Console
from rich.table import Table

from utils.system_info import get_system_info
from utils.plugins import get_plugins

console = Console()


def dashboard():

    info = get_system_info()

    table = Table(title="TS-OSINT Dashboard")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    for k, v in info.items():
        table.add_row(k, str(v))

    table.add_row("Modules", str(len(get_plugins())))

    console.print(table)
