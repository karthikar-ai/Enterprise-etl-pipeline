from database import SessionLocal
from db_models import CustomerDB
from database_loader import load_customers
from transformer import transform_customer


def test_customer_load():
    customer = transform_customer({
        "id": "TEST001",
        "name": " Database User ",
        "email": " DATABASE@EXAMPLE.COM ",
        "created_at": "2026-09-19T18:00:00"
    })

    load_customers([customer])

    db = SessionLocal()

    result = db.get(CustomerDB, "TEST001")

    assert result is not None
    assert result.name == "Database User"
    assert result.email == "database@example.com"

    db.close()