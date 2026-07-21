import platform
import socket
import sys


def get_system_info():
    return {
        "OS": platform.system(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "Python": sys.version.split()[0],
        "Hostname": socket.gethostname()
    }
