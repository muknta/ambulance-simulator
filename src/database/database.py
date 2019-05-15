import psycopg2
from ../../config import *


class DbConnector():
    def __init__(self):
        self.conn = psycopg2.connect(database=Config.database, host=Config.host, user=Config.user)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    def query(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()


class Views():
    def __init__(self):
        self.connect = DbConnector()

    def save_state(self, chat_id: str, state: int):
        try:
            self.connect.query('''insert into state(chat_id, state) values('{}', {})
                                  on conflict(chat_id) DO UPDATE SET state = excluded.state'''.format(chat_id, state))
        except 'InsertionError':
            print('Insertion or updating error')

    def get_state(self, chat_id):
        self.connect.query("select state from state where chat_id = '%s'" % chat_id)
        state = self.connect.cursor.fetchone()[0]
        return state

    def main_symptoms(self):
        self.connect.query('''select common_name
                      from symptoms
                      where name like '%pain' ''')
        return self.connect.cursor.fetchall()

    def abdominal_pain(self, pain: str):
        self.connect.query('''select common_name
                            from symptoms
                            where name like '{}%'
                            order by common_name'''.format(pain))
        return self.connect.cursor.fetchall()

