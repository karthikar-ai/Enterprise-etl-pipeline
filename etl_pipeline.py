from transformer import transform_json_file
from cleaner import clean_customer_data
from database_loader import load_customers


def run_pipeline():
    # Extract + Transform
    customers = transform_json_file(
        "raw_data/stripe_customers.json"
    )

    # Clean
    cleaned_data = clean_customer_data(
        [customer.model_dump() for customer in customers]
    )

    # Convert cleaned data back to Customer objects
    cleaned_customers = [
        customers[i].model_copy(
            update={
                "name": row["name"],
                "email": row["email"],
                "created_at": row["created_at"].to_pydatetime()
                if hasattr(row["created_at"], "to_pydatetime")
                else row["created_at"],
            }
        )
        for i, row in cleaned_data.iterrows()
    ]

    # Load
    load_customers(cleaned_customers)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()