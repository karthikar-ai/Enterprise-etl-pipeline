# Enterprise ETL Pipeline & Data Warehouse Synchronizer

## Overview

The Enterprise ETL Pipeline & Data Warehouse Synchronizer is a Python-based data engineering project designed to extract customer data from multiple sources, transform and clean the data into a unified format, and load it into a centralized database.

## Objective

The main objective of this project is to build a reliable and scalable ETL pipeline that can integrate data from different APIs while handling pagination, retries, data validation, cleaning, and incremental database loading.

## Technologies Used

- Python
- Requests
- Pydantic
- Pandas
- Tenacity
- AWS S3 / Boto3
- SQLAlchemy
- Pytest
- Git & GitHub

## Project Workflow

```text
Stripe API ───────┐
                  │
                  ▼
Salesforce API ──► Extract
                     │
                     ▼
                Raw Data / S3
                     │
                     ▼
              Clean & Transform
                     │
                     ▼
             Pydantic Validation
                     │
                     ▼
              Unified Customer
                     │
                     ▼
              Database Loading
                     │
                     ▼
                   Upsert