from wsgiref.simple_server import make_server, WSGIRequestHandler

from clock_app.server import app


class QuietHandler(WSGIRequestHandler):
    """Silent handler — no per-request logging."""
    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    with make_server("", 8000, app, handler_class=QuietHandler) as server:
        print("Server started at http://127.0.0.1:8000")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped")
