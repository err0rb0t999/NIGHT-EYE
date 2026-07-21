from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()


def loading(text="Loading", seconds=2):

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description}"),
        transient=True,
    ) as progress:

        task = progress.add_task(text, total=None)

        time.sleep(seconds)

        progress.remove_task(task)
