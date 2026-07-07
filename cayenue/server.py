import http.server
import socketserver
import os
import signal
import sys
from pathlib import Path
from PyQt6.QtCore import QStandardPaths
from loguru import logger

PORT = 8800

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

def getLogFilename():
    return os.path.join(getCacheLocation(), "server_logs", "server_logs.txt")

def handle_sigterm(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    disable_nagle_algorithm = True

    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.logger_id = logger.add(getLogFilename(), rotation="1 MB")
        logger.info(f"HTTP server started on port {PORT}, serving files from {getCacheLocation()}")

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
        logger.error(f"HTTP SERVER ERROR: {ex}")
