import phonenumbers
from phonenumbers import carrier, geocoder, timezone

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from utils.report import save_json, save_html
from utils.logger import info, error

console = Console()


def phone_parser():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Phone Number Parser[/bold cyan]\n"
            "[green]Public metadata only[/green]",
            border_style="cyan"
        )
    )

    number = input("\nEnter Phone Number (Example: +919876543210): ").strip()

    if not number:
        console.print("[red]Phone number cannot be empty.[/red]")
        return

    info(f"Phone Parser Request: {number}")

    try:
        parsed = phonenumbers.parse(number, None)

        valid = "Yes" if phonenumbers.is_valid_number(parsed) else "No"
        possible = "Yes" if phonenumbers.is_possible_number(parsed) else "No"

        country_code = f"+{parsed.country_code}"
        national_number = str(parsed.national_number)

        region = geocoder.description_for_number(parsed, "en") or "Unknown"
        network = carrier.name_for_number(parsed, "en") or "Unknown"

        zones = timezone.time_zones_for_number(parsed)
        timezone_name = ", ".join(zones) if zones else "Unknown"

        international = phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

        national = phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.NATIONAL
        )

        e164 = phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )

        data = {
            "Valid": valid,
            "Possible": possible,
            "Country Code": country_code,
            "National Number": national_number,
            "Region": region,
            "Carrier": network,
            "Timezone": timezone_name,
            "International": international,
            "National": national,
            "E164": e164,
        }

        table = Table(title="Phone Information")

        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")

        for key, value in data.items():
            table.add_row(key, str(value))

        console.print(table)

        try:
            json_file = save_json(data, "phone_report")
            html_file = save_html(data, "phone_report")

            console.print(
                f"[green]✔ JSON Report:[/green] {json_file}"
            )

            console.print(
                f"[green]✔ HTML Report:[/green] {html_file}"
            )

            info("Phone report exported successfully")

        except Exception as export_error:
            error(str(export_error))
            console.print(
                f"[yellow]Report export failed:[/yellow] {export_error}"
            )

    except phonenumbers.NumberParseException as e:
        error(str(e))
        console.print(f"[red]Invalid phone number:[/red] {e}")

    except Exception as e:
        error(str(e))
        console.print(f"[red]Unexpected error:[/red] {e}")
