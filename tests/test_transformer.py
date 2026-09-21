from transformer import transform_customer, map_to_unified_customer


def test_transform_customer():
    customer = {
        "id": "C001",
        "name": " Test User ",
        "email": " TEST@EXAMPLE.COM ",
        "created_at": "2026-09-19T18:00:00"
    }

    result = transform_customer(customer)

    assert result.customer_id == "C001"
    assert result.name == "Test User"
    assert result.email == "test@example.com"


def test_map_to_unified_customer():
    customer = {
        "id": "SF001",
        "name": " Test User ",
        "email": " TEST@EXAMPLE.COM ",
        "created_at": "2026-09-19T18:00:00"
    }

    result = map_to_unified_customer(customer)

    assert result.customer_id == "SF001"
    assert result.name == "Test User"
    assert result.email == "test@example.com"