import pandas as pd


def clean_customer_data(customers):
    df = pd.DataFrame(customers)

    df["name"] = df["name"].fillna("").str.strip()
    df["email"] = df["email"].fillna("").str.strip().str.lower()
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    return df