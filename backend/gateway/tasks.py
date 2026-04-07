from celery import shared_task
import time

@shared_task(bind=True, autoretry_for=(Exception,),
             retry_backoff=True,
             retry_kwargs={'max_retries': 5})
def send_to_external_api(self, customer_id, payload):

    print(f"Processing request from {customer_id}")

    # simulate API call
    time.sleep(1)

    return {"status": "success"}