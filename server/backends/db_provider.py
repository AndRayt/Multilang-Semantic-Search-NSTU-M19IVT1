import sqlite3
from sentence_transformers import SentenceTransformer, util
import torch

DB_PATH = r"../../web_service/db.sqlite3"


class DbProvider:
    def __init__(self, langs=('en',)):
        self.langs = langs
        self.connection = sqlite3.connect(DB_PATH)

    def get_phrases_by_lang(self, lang):
        if lang not in self.langs:
            raise ValueError('Incorrect language code name')
        with self.connection:
            cur = self.connection.cursor()
            command = "SELECT value FROM app_phrases \
                        INNER JOIN app_language on app_phrases.language_id = app_language.id \
                        WHERE app_language.name = '{0}'".format(lang)
            cur.execute(command)
            data = cur.fetchall()
            return [el[0] for el in data]