import requests
from config import STRIPE_API_KEY


def fetch_stripe_customers():
    url = "https://api.stripe.com/v1/customers"

    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()