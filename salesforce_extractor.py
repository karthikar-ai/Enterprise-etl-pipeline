import requests
from config import SALESFORCE_API_KEY


def fetch_salesforce_customers():
    url = "https://api.salesforce.com/services/data/v1/customers"

    headers = {
        "Authorization": f"Bearer {SALESFORCE_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()