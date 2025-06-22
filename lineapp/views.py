from django.http import HttpResponse
from .line_config import handler
from django.views.decorators.csrf import csrf_exempt
from . import webhook_handler

webhook_handler.handle_message


@csrf_exempt
def webhook_callback(request):
    if request.method == 'POST':
        signature = request.headers.get('X-Line-Signature')
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except Exception:
            return HttpResponse(status=400)

        return HttpResponse("OK")
    return HttpResponse("Only POST allowed", status=405)
