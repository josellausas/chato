"""
Chato v0.1 for easy PubSub Messaging
by Jose Llausas
"""
import os
from slack_sdk import WebClient

ENABLED = True
DEFAULT_CHANNEL = 'general'
DEFAULT_SLACK_NAME = "NAMELESS"

class _Chato:
    def __init__(self, token=None, slack_name=None):
        self.client = None
        self.enabled = True
        self.token = token or os.getenv("SLACK_TOKEN", "")
        self.slack_name = slack_name or os.getenv("SLACK_NAME", DEFAULT_SLACK_NAME)

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def chato(self, message, with_path='', channel=DEFAULT_CHANNEL):
        if not self.enabled:
            return 0
        if self.client is None:
            self.client = WebClient(token=self.token)
        return send_message_with_client(self.client, message, with_path, channel, self.slack_name)

INSTANCE = _Chato()

def getInstance():
    return INSTANCE

def send_message_with_client(client, message, with_path='', channel=DEFAULT_CHANNEL, slack_name=DEFAULT_SLACK_NAME):
    '''
    Sends a message to Slack
    '''
    if not ENABLED:
        return 0
    name_tag = f'[ {slack_name} | {with_path} ]'
    response = client.chat_postMessage(
        channel=f'#{channel}',
        text=f'{name_tag} {message}'
    )
    if response:
        return 0
    return -1

def chato(message, with_path='', channel=DEFAULT_CHANNEL):
    return INSTANCE.chato(message, with_path, channel)
