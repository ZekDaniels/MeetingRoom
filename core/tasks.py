from celery import shared_task



@shared_task()
def task_execute(job_params):
    print(job_params)
    print("Task executed")
    return job_params


@shared_task()
def add(x, y):
    return x + y    