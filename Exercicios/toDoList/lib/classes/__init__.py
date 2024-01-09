from datetime import datetime


class Tarefa:
    def __init__(self, title, date=str(datetime.now()), check="0"):
        self.title = title
        self.date = date
        self.check = check

    def __str__(self):
        return f'{self.title} {self.date} {self.check}'
