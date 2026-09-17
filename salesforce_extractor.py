import requests
from config import SALESFORCE_API_KEY


def fetch_salesforce_customers():
    url = "https://api.salesforce.com/services/data/v1/customers"

    headers = {
        "Authorization": f"Bearer {SALESFORCE_API_KEY}"
    }

    customers = []
    next_url = url

    while next_url:
        response = requests.get(next_url, headers=headers)

        response.raise_for_status()

        data = response.json()
        customers.extend(data.get("records", []))

        next_url = data.get("nextRecordsUrl")

        if next_url and next_url.startswith("/"):
            next_url = f"https://api.salesforce.com{next_url}"

    return customers