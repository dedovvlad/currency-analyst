import pytest


def test_get_currency_actual_some_items_positive(client):
    """Тест для проверки запроса без указания валюты."""
    response = client.get("/currency/actual")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize("currency", ["USD", "EUR"])
def test_get_currency_actual_one_item_positive(client, currency):
    """Тест для проверки запроса с указанием валюты."""
    response = client.get(url="/currency/actual/", params=f"currency_code={currency}")
    assert response.status_code == 200
    assert len(response.json()) < 2
    assert currency in response.json()
    assert isinstance(response.json().get(currency), float)


def test_give_unexisting_currence(client):
    """Негативный тест для проверки запроса с отсутствующей валютой."""
    response = client.get(url="/currency/actual", params="currency_code=MAD")
    assert response.status_code == 422
