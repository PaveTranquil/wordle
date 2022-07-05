from json import dumps, loads
from os import environ

from peewee import (IntegerField, Model, PostgresqlDatabase, SmallIntegerField,
                    TextField)
from playhouse.db_url import connect

from functions import get_new_word

conn: PostgresqlDatabase = connect(environ['DATABASE_URL'], sslmode='require')


class BaseModel(Model):
    class Meta:
        database = conn


class Player(BaseModel):
    id = IntegerField(primary_key=True)
    cword = TextField()
    guesses = SmallIntegerField(default=1)
    story = TextField(default='')
    uword = TextField(default='')
    used_letters = TextField(default='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    stats = TextField(default=dumps({i: 0 for i in (1, 2, 3, 4, 5, 6, 'wins', 'total')}))

    def new_game(self):
        self.cword = get_new_word()
        self.uword, self.guesses, self.story = '', 1, ''
        self.used_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.save()

    def increase_guesses(self):
        self.guesses += 1
        self.save()

    def win(self, guess):
        stats_from_bd = loads(self.stats)
        print(stats_from_bd)
        stats_from_bd[str(guess)] += 1
        stats_from_bd['wins'] += 1
        stats_from_bd['total'] += 1
        self.stats = dumps(stats_from_bd)
        self.new_game()

    def lose(self):
        stats_from_bd = loads(self.stats)
        stats_from_bd['total'] += 1
        self.stats = dumps(stats_from_bd)
        self.new_game()

    def get_stats(self):
        return loads(self.stats)

    class Meta:
        table_name = 'Data'


if __name__ == "__main__":
    response = input('Создаём таблицы? (Y/N) ').lower()
    if response == 'y':
        conn.create_tables([Player])
    # ПОЛЕ ДЛЯ СВОБОДНЫХ ЗАПРОСОВ
