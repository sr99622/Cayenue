import http.server
import socketserver
import os
import signal
import sys
from pathlib import Path
from PyQt6.QtCore import QStandardPaths

PORT = 8800

'''
if sys.platform == "win32":
    DIRECTORY = f"{os.environ['HOMEPATH']}/.cache/Cayenue/proxy"
else:
    DIRECTORY = f"{os.environ['HOME']}/.cache/Cayenue/proxy"

if sys.platform == "win32":
    DIRECTORY = f"{os.environ['HOMEPATH']}/.cache/Cayenue/proxy"
elif sys.platform == "darwin":
    DIRECTORY = Path(os.path.dirname(__file__)).parent.absolute() / "cache" / "proxy"
elif sys.platform.startswith("linux"):
    #DIRECTORY = f"{os.environ['HOME']}/.cache/Cayenue/proxy"
    DIRECTORY = "/home/stephen/github/Cayenue/env/lib/python3.13/site-packages/cayenue"
else:
    print(f"Unknown platform: {sys.platform}")
'''

def getLocation():
    path = Path(os.path.dirname(__file__))
    return str(path.parent.absolute())

def getCacheLocation():
    match sys.platform:
        case "linux":
            if len(QStandardPaths.standardLocations(QStandardPaths.StandardLocation.AppDataLocation)):
                return os.path.join(QStandardPaths.standardLocations(QStandardPaths.StandardLocation.AppDataLocation)[0], "cayenue", "proxy")
            else:
                return os.path.join(os.environ['HOME'], ".cache", "cayenue", "proxy")
        case "win32":
            return os.path.join(os.environ['HOMEPATH'], ".cache", "cayenue", "proxy")
        case "darwin":
            return os.path.join(getLocation(), "cache", "proxy")

    # fallback if all else fails
    return ".cache"



def handle_sigterm(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    disable_nagle_algorithm = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=getCacheLocation(), **kwargs)

    def do_POST(self):
        if self.path == "/shutdown":
            self.send_response(200)
            self.end_headers()
            self.server.shutdown()
        else:
            super().do_POST()

if __name__ == "__main__":
    try:
        with Server(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except Exception as ex:
        print(f"HTTP SERVER ERROR: {ex}")

