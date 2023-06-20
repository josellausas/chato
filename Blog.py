class BlogPost:
    def __init__(self, notionObj) -> None:
        self.original = notionObj

    def print_original(self):
        print(self.original)
