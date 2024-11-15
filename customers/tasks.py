from celery import shared_task
import pandas as pd
from .models import Customer
from django.db import IntegrityError

@shared_task
def ingest_customer_data(file_path):
    try:
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            customer_id = row['Customer ID']
            first_name = row['First Name']
            last_name = row['Last Name']
            age = row['Age']
            phone_number = row['Phone Number']
            monthly_salary = row['Monthly Salary']
            approved_limit = row['Approved Limit']
            # current_debt = row['current_debt']

            customer = Customer(
                customer_id=customer_id,
                first_name=first_name,
                last_name=last_name,
                age=age,
                phone_number=phone_number,
                monthly_salary=monthly_salary,
                approved_limit=approved_limit,
                # current_debt=current_debt
            )
            try:
                customer.save()
            except IntegrityError:
                print(f"Customer with ID {customer_id} already exists.")
                continue

        return f"Customer data ingestion completed successfully!"

    except Exception as e:
        return f"Error: {str(e)}"
