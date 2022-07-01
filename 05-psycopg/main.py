import psycopg2

def create_db(conn):
    pass

def add_client(conn, first_name, last_name, email, phones=None):
    pass

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="123", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        # удаление таблиц
        # cur.execute("""
        # DROP TABLE homework;
        # DROP TABLE course;
        # """)

        # создание таблиц
        cur.execute("""
        CREATE TABLE IF NOT EXISTS course(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) UNIQUE
        );
        """)
        conn.commit()  # фиксируем в БД
conn.close()