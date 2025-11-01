from datetime import datetime

from clock_app.services.time_service import TimeService


service = TimeService()


def test_valid_timezone():
    result = service.get_current_time("Europe/London")
    assert result["timezone"] == "Europe/London"
    datetime.strptime(result["formatted"], "%H:%M:%S")


def test_invalid_timezone_fallback():
    result = service.get_current_time("Fake/Zone")
    assert result["timezone"] == TimeService.DEFAULT_TZ
    datetime.strptime(result["formatted"], "%H:%M:%S")
