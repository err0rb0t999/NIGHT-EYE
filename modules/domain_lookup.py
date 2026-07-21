import socket
import whois
import dns.resolver

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from utils.logger import info, error
from utils.report import save_json, save_html

console = Console()


def get_dns(domain, record):

    try:
        answers = dns.resolver.resolve(domain, record)
        return [str(r) for r in answers]

    except Exception:
        return []


def domain_lookup():

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Domain Lookup[/bold cyan]\n"
            "[green]Public DNS & WHOIS Information[/green]",
            border_style="cyan"
        )
    )

    domain = input("\nEnter Domain (example.com): ").strip().lower()

    if not domain:
        return

    info(f"Domain Lookup : {domain}")

    try:

        ip = socket.gethostbyname(domain)

    except Exception:
        ip = "Unavailable"

    try:

        w = whois.whois(domain)

    except Exception:
        w = {}

    data = {
        "Domain": domain,
        "IP Address": ip,
        "Registrar": str(getattr(w, "registrar", "Unknown")),
        "Creation Date": str(getattr(w, "creation_date", "Unknown")),
        "Expiration Date": str(getattr(w, "expiration_date", "Unknown")),
        "Name Servers": ", ".join(getattr(w, "name_servers", []) or []),
        "A Record": ", ".join(get_dns(domain, "A")),
        "AAAA Record": ", ".join(get_dns(domain, "AAAA")),
        "MX Record": ", ".join(get_dns(domain, "MX")),
        "NS Record": ", ".join(get_dns(domain, "NS")),
        "TXT Record": ", ".join(get_dns(domain, "TXT")),
    }

    table = Table(title="Domain Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    for k, v in data.items():
        table.add_row(k, str(v) if v else "N/A")

    console.print(table)

    try:

        json_file = save_json(data, "domain_report")
        html_file = save_html(data, "domain_report")

        console.print(f"\n[green]✔ JSON:[/green] {json_file}")
        console.print(f"[green]✔ HTML:[/green] {html_file}")

    except Exception as e:

        error(str(e))
