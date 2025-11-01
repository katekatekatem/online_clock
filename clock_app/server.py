import json

from urllib.parse import parse_qs

from clock_app.logger_config import logger
from clock_app.routes import get_index_html, get_current_time_api


def serve_static_file(path: str) -> tuple[str, bytes, str]:
    """Read static file and return status, content, and content-type."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().encode("utf-8")

        if path.endswith(".css"):
            content_type = "text/css"
        elif path.endswith(".js"):
            content_type = "application/javascript"
        else:
            content_type = "text/plain"

        return "200 OK", content, content_type

    except FileNotFoundError:
        return "404 Not Found", b"404 Not Found", "text/plain"


def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    try:
        if path == "/":
            html = get_index_html()
            status = "200 OK"
            headers = [("Content-Type", "text/html; charset=utf-8")]
            body = html.encode("utf-8")

        elif path == "/api/time":
            query = parse_qs(environ.get("QUERY_STRING", ""))
            data = get_current_time_api(query)
            status = "200 OK"
            headers = [("Content-Type", "application/json")]
            body = json.dumps(data).encode("utf-8")

        elif path.startswith("/static/"):
            file_path = "clock_app" + path
            status, body, content_type = serve_static_file(file_path)
            headers = [("Content-Type", content_type)]

        else:
            status = "404 Not Found"
            body = b"404 Not Found"
            headers = [("Content-Type", "text/plain")]

    except Exception as e:
        logger.error("Server error: %s", e)
        status, headers, body = "500 Internal Server Error", [
            ("Content-Type", "text/plain")
        ], "500 Internal Server Error"

    start_response(status, headers)
    return [body]
