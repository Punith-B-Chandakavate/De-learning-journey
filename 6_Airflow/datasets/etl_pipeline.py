

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract(): 
    pass

def transform(): 
    pass

def load(): 
    pass

with DAG(
        'etl_pipeline',
        start_date=datetime(2025, 10, 20),
        schedule='0 2 * * *',  # Run daily at 2 AM
        ) as dag:
    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract,
        retries=3,
        retry_delay=timedelta(minutes=5),
    )

    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)

    t1 >> t2 >> t3