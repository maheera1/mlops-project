from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='ML Pipeline for Innovate Analytics',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

# Task 1: Data Preprocessing
preprocess_data = DockerOperator(
    task_id='preprocess_data',
    image='mlops-app:latest',
    command='python src/data/preprocess.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Task 2: Feature Engineering
feature_engineering = DockerOperator(
    task_id='feature_engineering',
    image='mlops-app:latest',
    command='python src/features/engineer.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Task 3: Model Training
train_model = DockerOperator(
    task_id='train_model',
    image='mlops-app:latest',
    command='python src/models/train.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Task 4: Model Evaluation
evaluate_model = DockerOperator(
    task_id='evaluate_model',
    image='mlops-app:latest',
    command='python src/models/evaluate.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Task 5: Model Deployment
deploy_model = DockerOperator(
    task_id='deploy_model',
    image='mlops-app:latest',
    command='python src/models/deploy.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Define task dependencies
preprocess_data >> feature_engineering >> train_model >> evaluate_model >> deploy_model 