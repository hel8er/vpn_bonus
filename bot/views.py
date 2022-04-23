from .models import TgUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .schemas import Update
from .logic import cmd_list, bot


class WebhookView(APIView):
    queryset = TgUser.objects.all()

    def post(self, request):
        res = 0
        update = Update(**request.data)

        if update.message.text.startswith('/'):
            for cmd_class in cmd_list:

                if update.message.text.startswith(cmd_class.text):
                    cmd = cmd_class()
                    res = cmd.run(update)
        else:
            res = bot.forward_message(update.message.chat.id, 100136652, update.message.message_id)

        return Response({'result': str(res)})


