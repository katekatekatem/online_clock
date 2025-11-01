from clock_app.routes import build_timezone_options, get_current_time_api
from clock_app.services.time_service import TimeService


def test_build_timezone_options_returns_string():
    html = build_timezone_options()
    assert isinstance(html, str)
    assert "<option" in html


def test_get_current_time_api_invalid_fallback():
    query = {"tz": ["Non/Existing"]}
    result = get_current_time_api(query)
    assert result["timezone"] == TimeService.DEFAULT_TZ
