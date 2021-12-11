import sqlite3


def create_items_table(conn):
    """
    Creates the items table in sqlite if it
    does not exist already
    """
    sql_command = """ CREATE TABLE IF NOT EXISTS items (
                            id integer PRIMARY KEY,
                            name text NOT NULL UNIQUE,
                            quantity integer
                        );"""
    cursor = conn.cursor()
    try:
        cursor.execute(sql_command)
    except Exception as e:
        print(e)


def create_item_tuple():
    """ 
    Takes in user input and returns a tuple of an item
    """
    user_input = input("Enter item (name quantity): ")
    item = tuple(user_input.split())
    if len(item) == 2:
        return item
    else:
        print("Too many arguments provided to item")


def insert_item(conn, item):
    """
    Inserts item in tuple format to database
    """
    sql_command = """INSERT INTO items (name, quantity)
                    VALUES(?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql_command, item)
    conn.commit()


def delete_item(conn, item_name):
    """
    Delete row that matches item_name
    """
    sql_command = "DELETE FROM items WHERE name = ?"
    cursor = conn.cursor()
    result = cursor.execute(sql_command, (item_name,))
    conn.commit()
    if result.rowcount > 0:
        print("Item was successfully deleted")
    else:
        print("No item was deleted")


def update_item_quantity(conn, item_name, quantity):
    """
    Update quantity to argument when it matches item_name
    """
    sql_command = "UPDATE items SET quantity = ? WHERE name = ?"
    cursor = conn.cursor()
    result = cursor.execute(sql_command, (quantity, item_name))
    conn.commit()
    if result.rowcount > 0:
        print("Item was successfully updated")
    else:
        print("No item was updated")


def display(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items ORDER BY name")
    rows = cursor.fetchall()
    print("=" * 28)
    print(f"{'Name':<15}{'Quantity':<10}")
    for row in rows:
        name = row[1]
        quantity = row[2]
        print(f"{name:<15}{quantity:<10}")


def main():
    db_file = "./order.db"
    conn = sqlite3.connect(db_file)
    create_items_table(conn)
    display(conn)
    input()
    insert_item(conn, create_item_tuple())


if __name__ == "__main__":
    main()
