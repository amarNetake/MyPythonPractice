from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import prac 

from datetime import datetime

default_args = {
    'owner':'amar_netake',
    'start_date':datetime(2022,3,28),
    'retries':2
}

my_trial= DAG(dag_id='trial_dag', default_args=default_args, schedule_interval='* * * * *', catchup=False)

def createObj():
    obj=prac.myself()
    return obj

def gen_email(ti):
    obj=ti.xcom_pull(task_id='create_object')
    obj.yob()
    return obj

def fwrite(ti):
    obj=ti.xcom_pull(task_id='email_generation')
    obj.write_to_file()

create_obj = PythonOperator(
    task_id='create_object',
    python_callable='createObj',
    dag=my_trial
)

generate_email = BranchPythonOperator(
    task_id='email_generation',
    python_callable='gen_email',
    dag=my_trial
)

write_to_file = BranchPythonOperator(
    task_id='writing_in_file',
    python_callable='fwrite',
    dag=my_trial
)

create_obj>>generate_email>>write_to_file