from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 

def extract():
    print("Extracted successfully")

def transform():
    print("Transformed successfully")

def load():
    print("Loaded successfully")

with DAG(
    dag_id = 'test_pipeline_demo',
    start_date = datetime(26,2,1),
    schedule = "@daily",
    catchup = False,
    tags = ['demo']
) as dag:
    
    extract_task = PythonOperator(
        task_id = 'Extract',
        python_callable = extract
    )

    transform_task = PythonOperator(
        task_id = 'Transform',
        python_callable = transform
    )

    load_task = PythonOperator(
        task_id = 'Load',
        python_callable = load 
    )

    extract_task >> transform_task >> load_task
