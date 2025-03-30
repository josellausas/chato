import os
import logging
from notion_client import Client, APIErrorCode, APIResponseError
from dotenv import load_dotenv

config = load_dotenv("josellausas/.env")


class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)): 
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value


class NotionTool:
    def __init__(self) -> None:
        self.notion = Client(auth=os.environ["NOTION_TOKEN"])
        self.BLOG_DB_ID = os.environ["NOTAPI_BLOG_DB"]
        self.TOGGLES_DB_ID = os.environ["NOTAPI_TOGGLES_DB"]

    def get_blog(self):
        my_db = None
        try:
            my_db = self.notion.databases.query(
                **{
                    "database_id": self.BLOG_DB_ID,
                }
            )
        except APIResponseError as error:
            if error.code == APIErrorCode.ObjectNotFound:
                raise FileExistsError("Dabase does not exist")
            else:
                # Other error handling code
                logging.error(error)
        return my_db
        # print(my_db)
        # return Struct(my_db).results

    def get_toggles(self):
        my_db = None
        try:
            my_db = self.notion.databases.query(
                **{
                    "database_id": self.TOGGLES_DB_ID,
                }
            )
        except APIResponseError as error:
            if error.code == APIErrorCode.ObjectNotFound:
                raise FileExistsError("Dabase does not exist")
            else:
                # Other error handling code
                logging.error(error)
        return Struct(my_db).results

    def get_toggle_status(self, toggle):
        return toggle.properties.Status.status.name

    def get_toggle_name(self, toggle):
        return toggle.properties.Name.title[0]['plain_text']

    def is_enabled(self, toggle):
        return self.get_toggle_status(toggle) == 'Production' or 'Develop'

    def get_and_print_toggles(self):
        toggles = self.get_toggles()
        for t in toggles:
            print(self.get_toggle_name(t))
            print(self.get_toggle_status(t))


class Domain:
    def __init__(self, name, is_live) -> None:
        self.name = name
        self.is_live = True if is_live else False

    def __repr__(self) -> str:
        return self.name
