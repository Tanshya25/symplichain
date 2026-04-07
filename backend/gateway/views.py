from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_to_external_api

@api_view(["POST"])
def submit_request(request):

    customer_id = request.data.get("customer_id")
    payload = request.data.get("payload")

    send_to_external_api.delay(customer_id, payload)

    return Response({"message": "Queued successfully"})