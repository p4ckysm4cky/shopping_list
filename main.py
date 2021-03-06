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
    while True:
        user_input = input("Enter item in format (name, quantity): ")
        item = tuple(user_input.split(','))
        item = tuple([value.strip() for value in item])
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

def delete_all_item(conn):
    """
    Deletes all rows from the items table
    """
    sql_command = "DELETE FROM items"
    user_input = input("Type YES if you are sure you want to remove all items: ")
    if user_input == "YES":
        cursor = conn.cursor()
        cursor.execute(sql_command)
        conn.commit()
    else:
        return


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
    """
    Displays the item stored in the database
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items ORDER BY name")
    rows = cursor.fetchall()
    print("=" * 28)
    print(f"{'Name':<15}{'Quantity':<10}")
    for row in rows:
        name = row[1]
        quantity = row[2]
        print(f"{name:<15}{quantity:<10}")
    print("=" * 28)
    print()


def menu(conn):
    """
    Displays a menu with options for the user to choose
    """
    print("""Please choose the following options:
    1: Add new item to list
    2: Delete item from list
    3: Update item quantity
    4: Delete all items from list
    99: Exit""")
    user_selection = input("").strip()
    if user_selection == '1':
        print("Insertion| ", end="")
        insert_item(conn, create_item_tuple())
        return 1
    elif user_selection == '2':
        item_name = input("Please enter the name of item you wish to delete: ")
        delete_item(conn, item_name)
        return 2
    elif user_selection == '3':
        print("Update| ", end="")
        update_item_quantity(conn, *create_item_tuple())
        return 3
    elif user_selection == '4':
        delete_all_item(conn)
    elif user_selection == '99':
        return 99
    else:
        print("Invalid option was chosen")
        return 0


def main():
    db_file = "./order.db"
    conn = sqlite3.connect(db_file)

    display(conn)
    user_option = menu(conn)
    while user_option != 99:
        display(conn)
        user_option = menu(conn)
    conn.close()


if __name__ == "__main__":
    main()
