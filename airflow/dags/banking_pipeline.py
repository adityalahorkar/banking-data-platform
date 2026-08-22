# Optional: runs the same pipeline as run_pipeline.py, on a schedule.

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_ROOT = "/opt/airflow/project"

with DAG(
    dag_id="banking_transaction_pipeline",
    description="Banking transaction pipeline: ingest, transform, load, report",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["banking", "etl"],
) as dag:

    steps = [
        "step1_create_database",
        "step2_create_schemas",
        "step3_profile_data",
        "step4_load_raw_data",
        "step5_transform_data",
        "step6_build_warehouse",
        "step7_create_analytics_views",
    ]

    tasks = [
        BashOperator(
            task_id=step,
            bash_command=f"cd {PROJECT_ROOT} && python -m pipeline.{step}",
        )
        for step in steps
    ]

    for i in range(len(tasks) - 1):
        tasks[i] >> tasks[i + 1]
