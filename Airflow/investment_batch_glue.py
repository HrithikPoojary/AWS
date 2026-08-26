from airflow import DAG #type:ignore
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator #type:ignore
from datetime import datetime, timedelta

default_args = {
    "user" : "airflow",
    "depends_on_past" : False,
    "retires" : 1,
    "retry_delay" : timedelta(minutes=5)
}

with DAG(
    dag_id = 'Investment_Batch_Glue',
    start_date = datetime(26,1,1),
    default_args = default_args,
    schedule = "@daily",
    catchup = False,
    tags = ['glue']

) as dag:
    
    eod_stg = GlueJobOperator(
        task_id  = "Eod_Stg_Task",
        glue_job_name = "EodStagingProcessor",
        region_name = "us-east-1",
        wait_for_completion = True,
        verbose = True
    )

    eod_quantity = GlueJobOperator(
        task_id = "Eod_Quantity_Task",
        glue_job_name = "EodQuantityProcessor",
        region_name = 'us-east-1',
        wait_for_completion = True,
        verbose = True 
    )

    eod_market_value = GlueJobOperator(
        task_id = "Eod_Market_Value_Task",
        glue_job_name = "EodMarketValue",
        region_name = 'is-east-1',
        wait_for_completion = True,
        verbose = True 
    )

    eod_stg >> eod_quantity >> eod_market_value