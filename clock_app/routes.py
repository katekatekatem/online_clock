import pytz

from datetime import datetime, date
from typing import List

from clock_app.logger_config import logger
from clock_app.services.time_service import TimeService


time_service = TimeService()

_cached_timezone_options: str = ""
_cached_date: date = None


def get_index_html() -> str:
    """Return HTML page with timezone dropdown."""
    try:
        with open("clock_app/templates/index.html", "r", encoding="utf-8") as f:
            template = f.read()
        options = build_timezone_options()
        return template.replace("{TIMEZONE_OPTIONS}", options)
    except FileNotFoundError:
        return "404 Not Found"


def build_timezone_options() -> str:
    """Build timezone dropdown HTML, cache per day."""
    global _cached_timezone_options, _cached_date
    today = date.today()
    if _cached_timezone_options and _cached_date == today:
        return _cached_timezone_options

    now_utc = datetime.utcnow()
    tz_data: List = []

    for tz_name in pytz.all_timezones:
        tz = pytz.timezone(tz_name)
        try:
            local_dt = pytz.utc.localize(now_utc).astimezone(tz)
            offset = local_dt.utcoffset()
            if offset is None:
                continue

            total_minutes = int(offset.total_seconds() / 60)
            hours, minutes = divmod(abs(total_minutes), 60)
            sign = "+" if total_minutes >= 0 else "-"
            offset_str = f"UTC{sign}{hours:02d}:{minutes:02d}"
            label = f"{offset_str} — {tz_name.replace('_', ' ')}"

            tz_data.append((total_minutes, tz_name, label))
        except Exception as e:
            logger.error("Failed to process timezone %s: %s", tz_name, e)

    tz_data.sort(key=lambda x: x[0])
    _cached_timezone_options = "\n".join(
        f'<option value="{tz_name}">{label}</option>' for _, tz_name, label in tz_data
    )
    _cached_date = today
    return _cached_timezone_options


def get_current_time_api(query: dict) -> dict:
    """Return current time JSON data for given timezone."""
    tz_name = query.get("tz", ["Asia/Jerusalem"])[0]
    data = time_service.get_current_time(tz_name)
    return data
