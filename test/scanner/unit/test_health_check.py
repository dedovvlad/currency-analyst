from src.scanner.api.health_check import get_health_check


def test_dealth_ceck():
    """Тест на проверку хелсчека."""
    response = {"status": "OK"}
    assert get_health_check() == response
