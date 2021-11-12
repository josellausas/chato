"""
Chato v0.1 for easy PubSub Messaging
by Jose Llausas
"""
import slack

from django.conf import settings

ENABLED = True

class _Chato:
    client = None
    enabled = True

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def chato(self, message, with_path='', channel='herrsil'):
        if not self.enabled:
            return 0

        if self.client is None:
            self.client = self.client = slack.WebClient(token=settings.SLACK_TOKEN)
        return send_message_with_client(self.client, message, with_path, channel)


INSTANCE = _Chato()

def getInstance():
    return INSTANCE


def send_message_with_client(client, message, with_path='', channel='herrsil'):
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

def chato(message, with_path='', channel='herrsil'):
    return INSTANCE.chato(message, with_path, channel)
