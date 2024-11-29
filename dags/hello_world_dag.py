from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id='hello_world', start_date=datetime(2022,1,1), schedule_interval="0 * * * *") as dag:
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def world():
        print('world')

    hello >> world()
