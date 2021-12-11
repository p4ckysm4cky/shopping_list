import sqlite3


def create_items_table(conn):
    sql_command = """ CREATE TABLE IF NOT EXISTS items (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            quantity integer
                        );"""
    cursor = conn.cursor()
    try:
        cursor.execute(sql_command)
    except Exception as e:
        print(e)


def main():
    db_file = "./order.db"
    conn = sqlite3.connect(db_file)
    create_items_table(conn)


if __name__ == "__main__":
    main()
