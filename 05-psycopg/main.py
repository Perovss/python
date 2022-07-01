import psycopg2

def create_db(conn):
        # удаление таблиц
        # cur.execute("""
        # DROP TABLE client CASCADE;
        # DROP TABLE phone CASCADE;
        # """)

        # создание таблиц
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(40),
            email VARCHAR(40) UNIQUE
        );
        CREATE TABLE IF NOT EXISTS phone(
            id SERIAL,
            client_id SERIAL PRIMARY KEY,
            phone VARCHAR(40) UNIQUE
        );
        ALTER TABLE ONLY public.phone
            ADD CONSTRAINT phone_fk FOREIGN KEY (client_id) REFERENCES public.client(id);
        
        COMMENT ON TABLE public.client IS 'Клиенты телефонной книги';
        COMMENT ON COLUMN public.client.id IS 'Идентификатор клиента';
        COMMENT ON COLUMN public.client.first_name IS 'Имя';
        COMMENT ON COLUMN public.client.last_name IS 'Фамилия';
        COMMENT ON COLUMN public.client.email IS 'Почтовый ящик';            
        COMMENT ON TABLE public.phone IS 'Телефонная книга';
        COMMENT ON COLUMN public.phone.id IS 'Идентификатор номера';
        COMMENT ON COLUMN public.phone.client_id IS 'Идентификатор клиента номера';
        COMMENT ON COLUMN public.phone.phone IS 'Номер телефона';
        """)
        conn.commit()  # фиксируем в БД


def add_client(conn, first_name, last_name, email):
# def add_client(conn, first_name, last_name, email, phones=None):
        cur.execute("""
        INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING id;
        """, (first_name, last_name, email))
        print(cur.fetchone()) 

def add_phone(conn, client_id, phone):
        cur.execute("""
        INSERT INTO phone(client_id, phone) VALUES(%s, %s) RETURNING id;
        """, (client_id, phone))
        print(cur.fetchone()) 

# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
def change_client(conn, id, first_name=None, last_name=None, email=None):    
        cur.execute("""
        UPDATE client SET first_name=%s,last_name=%s WHERE id=%s;
        """, (first_name, last_name, id))
        cur.execute("""
        SELECT * FROM client;
        """)
        print(cur.fetchall()) 

def delete_phone(conn, client_id, phone):
        cur.execute("""
        DELETE FROM phone WHERE id=%s AND phone=%s;
        """, (client_id, phone))
        cur.execute("""
        SELECT * FROM phone;
        """)
        print(cur.fetchall())

# def delete_client(conn, client_id):
def delete_client(conn, first_name=None, last_name=None, email=None):

        cur.execute("""
        DELETE FROM phone WHERE client_id IN (SELECT id FROM public.client WHERE first_name=%s AND last_name=%s OR email=%s);
        """, (first_name, last_name, email))
        cur.execute("""
        DELETE FROM client WHERE first_name=%s AND last_name=%s OR email=%s;
        """, (first_name, last_name, email))
        cur.execute("""
        SELECT * FROM phone;
        """)
        print(cur.fetchall())

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="client", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        # create_db(conn)
        # add_client(conn, 'Сергей','Перов','perov.ss@gmail.com')
        # add_phone(conn, 8, '+79992073199')
        # change_client(conn, 1, 'Вася', 'Пупкин') 
        # delete_phone(conn, 1, '+79992073199')
        delete_client(conn, '', '','perov.ss@gmail.com')
conn.close()