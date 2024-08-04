from airflow.models import DAG  
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

practice_dag = DAG(dag_id = "prac_dag", default_args={"start_date":datetime(2022,4,21), catchup=False}, schedule_interval="* * * * *")

def helloWorld():
    print("Hello World!!!") 

def pqr():
    print("This function is PQR")

def abc():
    print("This function is ABC")

part1 =PythonOperator(task_id="HW", python_callable="helloWorld",dag=practice_dag)
part2 =PythonOperator(task_id="random1", python_callable="pqr",dag=practice_dag)
part3 =PythonOperator(task_id="random2", python_callable="abc",dag=practice_dag)

part2>>part3>>part1

