import urllib.parse
from .schemas import Update
import requests


class Command:
    text = ''

    def run(self, update: Update):
        """method to ovverride"""
        pass


class Webhook:

    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.commands = {cmd.text: cmd for cmd in Command.__subclasses__()}

    def request(self, method, **params):
        url = self.base_url + method
        if params:

            params_str = '?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)

            url += params_str

            response = requests.request("GET", url,)
            return response.json()

    def get_me(self):
        info = self.request('getMe')
        return info

    def forward_message(self, from_id: int, to_id: int, msg_id: int):
        res = self.request('forwardMessage', chat_id=to_id, from_chat_id=from_id, message_id=msg_id)
        return res

    def send_message(self, chat_id: int, message: str):
        res = self.request('sendMessage', chat_id=chat_id, text=message)
        return res

    def set_webhook(self, url):
        return self.request('setWebhook', url=url)

    def delete_webhook(self):
        return self.request('deleteWebhook')

    def webhook_info(self):
        info = self.request('getWebhookInfo')
        print(info)
        return info
