#!/usr/bin/env python
import sys
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Slack Hello World
from slack_sdk import WebClient
client = WebClient()
api_response = client.api_test()
