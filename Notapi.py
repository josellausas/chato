import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
blog_database_id = os.environ["NOTION_DB"]

def get_blog():
    my_db = notion.databases.query(
        **{
            "database_id": blog_database_id,
        }
    )
    return my_db


class Domain:
    def __init__(self, name, is_live) -> None:
        self.name = name
        self.is_live = True if is_live else False
    
    def __repr__(self) -> str:
        return self.name

# TODO: Implmenet this using the NAPI Domains
domains = {
    'llau.systems': Domain('llau.systems', True),
    'josellausas.com': Domain('llau.systems', False),
}

def is_domain_live(domainId) -> bool:
    domain = domains[domainId]
    if domain:
        return domain.is_live
    
    return False

