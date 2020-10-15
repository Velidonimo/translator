"""
Saves translates to database
"""
import sqlite3, datetime, json, re


def save_translate(engl, rus):
    """Save a translate to database
    engl: english word
    rus: translate to russian
    """
    try:
        with open('data.json', encoding='utf-8') as file:
            data = json.load(file)
    except:
        print("Can't open data.json")
        return

    engl = _delete_quotes(engl)
    rus = _delete_quotes(rus)

    _create_db(data['sql']['name'], f"id INTEGER PRIMARY KEY, {data['sql']['engl']} TEXT, {data['sql']['rus']} TEXT, {data['sql']['time']} TEXT")
    _add_record(data['sql']['name'], engl, rus)

    # test
    _print_db(data['sql']['name'])


def _delete_quotes(word):
    """Delete quotes from a string to avoid problems in SQL queues"""
    word = re.sub('"', '', word)
    word = re.sub("'", "", word)
    return word


def _establish_coonection_decorator(query_func):
    """Establish connection and close it"""
    def establish_connection(*args):
        con = sqlite3.connect('history.db')
        cursor = con.cursor()
        query = query_func(*args)
        cursor.execute(query)
        con.commit()
        con.close()
    return establish_connection


@_establish_coonection_decorator
def _add_record(name, engl, rus):
    """Add record to database"""
    time = str(datetime.datetime.now().strftime('%Y-%M-%d/%H-%M'))
    return f"INSERT INTO history VALUES(NULL, '{engl}', '{rus}', '{time}')"


@_establish_coonection_decorator
def _create_db(name, columns):
    """Create new database"""
    return f'CREATE TABLE IF NOT EXISTS {name} ({columns})'


def _print_db(name):
    """Prints database content"""
    con = sqlite3.connect('history.db')
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {name}')
    rows = cursor.fetchall()
    con.close()

    for row in rows:
        print(row)
    print('===========')


if __name__ == '__main__':
    _print_db('history')