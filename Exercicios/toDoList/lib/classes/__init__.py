from datetime import datetime


class Tarefa:
    def __init__(self, title, date=datetime.now(), check=False):
        self.title = title
        self.date = date
        self.check = check
