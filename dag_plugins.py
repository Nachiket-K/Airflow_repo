from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import NachiketGitOperator


default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


t1 = NachiketGitOperator(
        task_id='git_clone',
        source_file_path = 'https://github.com/Nachiket-K/Airflow_Terraform.git',
        dag=dag
    )
