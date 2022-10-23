"""
Chato v0.1 for easy PubSub Messaging
by Jose Llausas
"""
from slack_sdk import WebClient

from django.conf import settings

ENABLED = True
DEFAULT_CHANNEL='general'

class _Chato:
    client = None
    enabled = True

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def chato(self, message, with_path='', channel=DEFAULT_CHANNEL):
        if not self.enabled:
            return 0

        if self.client is None:
            self.client = self.client = WebClient(token=settings.SLACK_TOKEN)
        return send_message_with_client(self.client, message, with_path, channel)


INSTANCE = _Chato()

def getInstance():
    return INSTANCE


def send_message_with_client(client, message, with_path='', channel=DEFAULT_CHANNEL):
    '''
    Sends a message to Slack
    '''
    if not ENABLED:
        return 0

    name_tag = f'[ {settings.SLACK_NAME} | {with_path} ]'
    response = client.chat_postMessage(
        channel=f'#{channel}',
        text=f'{name_tag} {message}'
    )
    if response:
        return 0
    return -1

def chato(message, with_path='', channel=DEFAULT_CHANNEL):
    return INSTANCE.chato(message, with_path, channel)
