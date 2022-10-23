import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
blog_database_id = os.environ["NOTION_DB"]

## TODO: Implement Notion
class NotionPage:
    def __init__(self) -> None:
        pass

class NotionBlock:
    def __init__(self) -> None:
         pass
    # block_id = '380c78c0-e0f5-4565-bdbd-c4ccb079050d'
    block_type = ''
    created_time = ''
    last_edited_time = ''
    has_children = False


class NotionDatabase:
    def __init__(self, payload) -> None:
        self.title = {}
        self.properties = {
            'Published': payload['properties']['Published']['checkbox']
        }

def get_page_with_id(page_id):
    my_page = notion.blocks.children.list(page_id)
    blocks = notion.blocks.retrieve(page_id)
    return my_page