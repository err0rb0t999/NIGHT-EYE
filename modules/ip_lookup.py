import ipaddress
import socket
import requests

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from utils.logger import info, error
from utils.report import save_json, save_html

console = Console()


def ip_lookup():

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Public IP Information[/bold cyan]",
            border_style="cyan"
        )
    )

    ip = input("\nEnter IPv4 / IPv6 : ").strip()

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        console.print("[red]Invalid IP Address[/red]")
        return

    info(f"IP Lookup : {ip}")

    try:

        hostname = socket.gethostbyaddr(ip)[0]

    except Exception:

        hostname = "Unavailable"

    try:

        response = requests.get(
            f"https://ipinfo.io/{ip}/json",
            timeout=10
        )

        result = response.json()

    except Exception as e:

        error(str(e))

        console.print("[red]Unable to fetch IP information[/red]")

        return

    data = {

        "IP": ip,
        "Hostname": hostname,
        "City": result.get("city", "Unknown"),
        "Region": result.get("region", "Unknown"),
        "Country": result.get("country", "Unknown"),
        "Location": result.get("loc", "Unknown"),
        "Organization": result.get("org", "Unknown"),
        "Postal": result.get("postal", "Unknown"),
        "Timezone": result.get("timezone", "Unknown")
    }

    table = Table(title="IP Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    for k, v in data.items():
        table.add_row(k, str(v))

    console.print(table)

    try:

        json_file = save_json(data, "ip_report")
        html_file = save_html(data, "ip_report")

        console.print(f"\n[green]✔ JSON :[/green] {json_file}")
        console.print(f"[green]✔ HTML :[/green] {html_file}")

    except Exception as e:

        error(str(e))

