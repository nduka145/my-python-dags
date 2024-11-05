from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    'new_copy_fstab',
    default_args=default_args,
    description='A DAG to copy /etc/fstab to /root every 30 minutes',
    schedule_interval='@daily',
    start_date=datetime(2024, 11, 4),
    catchup=False,
) as dag:

    # Define the task
    new_fstab = BashOperator(
        task_id='new_fstab',
        bash_command='cp /etc/fstab /root/fstab_copy',
    )
