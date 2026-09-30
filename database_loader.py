from database import SessionLocal
from db_models import CustomerDB


def load_customers(customers):
    db = SessionLocal()

    try:
        for customer in customers:
            existing = db.get(CustomerDB, customer.customer_id)

            if existing:
                existing.name = customer.name
                existing.email = customer.email
                existing.created_at = customer.created_at
            else:
                db_customer = CustomerDB(
                    customer_id=customer.customer_id,
                    name=customer.name,
                    email=customer.email,
                    created_at=customer.created_at
                )

                db.add(db_customer)

        db.commit()

    finally:
        db.close()