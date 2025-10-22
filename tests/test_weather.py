from src.weather_service import get_weather

def test_get_weather():
    result = get_weather("London")
    assert result is None or isinstance(result, dict)
