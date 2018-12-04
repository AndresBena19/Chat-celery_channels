from celery import current_app
from channels.layers import get_channel_layer
app = current_app
from asgiref.sync import async_to_sync

@app.task()
def hello():

    channel_layer = get_channel_layer()
    print(channel_layer)
    async_to_sync(channel_layer.group_send)("chat_default", {'type': 'chat_message', "message": "celery_msn"})

    return "hello word"
