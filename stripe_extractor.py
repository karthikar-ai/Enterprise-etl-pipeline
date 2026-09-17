import requests
from config import STRIPE_API_KEY

import requests
from config import STRIPE_API_KEY


def fetch_stripe_customers():
    url = "https://api.stripe.com/v1/customers"

    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}"
    }

    customers = []
    starting_after = None

    while True:
        params = {
            "limit": 100
        }

        if starting_after:
            params["starting_after"] = starting_after

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        response.raise_for_status()

        data = response.json()
        customers.extend(data["data"])

        if not data["has_more"]:
            break

        starting_after = data["data"][-1]["id"]

    return customers