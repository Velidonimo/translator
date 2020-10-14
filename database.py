import sqlite3, datetime


def establish_coonection_decorator(func):
    def establish_connection(*args):
        con = sqlite3.connect('history.db')
        cursor = con.cursor()
        query = func(*args)
        print(query)
        cursor.execute(query)
        con.close()
    return establish_connection

@establish_coonection_decorator
def add_record(engl, rus):
    time = str(datetime.datetime.now().strftime('%Y-%M-%d--%H-%M'))
    return f'INSERT INTO history VALUES(NULL, {engl}, {rus}, {time})'


@establish_coonection_decorator
def create_db(columns):
    return f'CREATE TABLE IF NOT EXISTS history ({columns})'



def read_db():
    con = sqlite3.connect('history.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM history')
    rows = cursor.fetchall()
    con.close()
    return rows


if __name__ == '__main__':
    create_db('id INTEGER PRIMARY KEY, engl TEXT, rus TEXT, time TEXT')
    add_record('apple', 'яблоко')
    for result in read_db():
        print(result)
