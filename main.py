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


def create_item_tuple():
    user_input = input("Enter item (name quantity): ")
    item = tuple(user_input.split())
    if len(item) == 2:
        return item
    else:
        print("Too many arguments provided to item")


def insert_item(conn, item):
    sql_command = """INSERT INTO items (name, quantity)
                    VALUES(?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql_command, item)
    conn.commit()


def main():
    db_file = "./order.db"
    conn = sqlite3.connect(db_file)
    create_items_table(conn)
    insert_item(conn, create_item_tuple())


if __name__ == "__main__":
    main()
