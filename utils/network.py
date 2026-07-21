import requests


def internet_available(timeout=5):
    """
    Check if internet connection is available.
    Returns True or False.
    """
    try:
        requests.get("https://1.1.1.1", timeout=timeout)
        return True
    except Exception:
        return False
