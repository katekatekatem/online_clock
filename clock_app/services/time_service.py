import pytz

from datetime import datetime

from clock_app.logger_config import logger


class TimeService:
    """Service to provide current time for given timezone."""

    DEFAULT_TZ = "Asia/Jerusalem"

    def get_current_time(self, tz_name: str) -> dict:
        """Return current time and timezone name."""
        try:
            tz = pytz.timezone(tz_name)
        except Exception as e:
            logger.error("Failed to get time for %s: %s", tz_name, e)
            tz_name = self.DEFAULT_TZ
            tz = pytz.timezone(tz_name)

        now = datetime.now(tz)
        formatted = now.strftime("%H:%M:%S")
        return {
            "timezone": tz_name,
            "formatted": formatted
        }
