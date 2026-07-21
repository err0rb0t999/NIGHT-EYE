import importlib
import sys

REQUIRED_MODULES = [
    "rich",
    "requests"
]


def check_dependencies():
    """
    Verify required Python packages are installed.
    """
    missing = []

    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(module)

    return missing


def quit_program():
    print("\nGoodbye!\n")
    sys.exit(0)
