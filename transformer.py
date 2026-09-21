from models import Customer
def transform_customer(customer):
    transformed = {
        "customer_id": customer.get("id"),
        "name": customer.get("name", "").strip(),
        "email": customer.get("email", "").strip().lower(),
        "created_at": customer.get("created_at")
    }

    return Customer(**transformed)
def transform_customers(customers):
    return [transform_customer(customer) for customer in customers]
def transform_json_file(file_path):
    import json

    with open(file_path, "r") as file:
        data = json.load(file)

    return transform_customers(data["data"])
def transform_salesforce_json_file(file_path):
    import json

    with open(file_path, "r") as file:
        data = json.load(file)

    return transform_customers(data["records"])
def map_to_unified_customer(customer):
    return Customer(
        customer_id=customer.get("customer_id") or customer.get("id"),
        name=customer.get("name", "").strip(),
        email=customer.get("email", "").strip().lower(),
        created_at=customer.get("created_at")
    )
         