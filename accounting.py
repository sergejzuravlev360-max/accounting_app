import sqlite3

# Читаем SQL-схему из файла
with open('schema.sql', 'r', encoding='utf-8') as f:
    schema = f.read()

# Создаём базу и выполняем схему
conn = sqlite3.connect('finance.db')
conn.executescript(schema)
conn.commit()
conn.close()

print('Database created successfully')


def get_connection():
    """Return a connection to the database."""
    return sqlite3.connect('finance.db')


def get_categories():
    """Return all categories as a list of (id, name)."""
    conn = get_connection()
    rows = conn.execute("SELECT id, name FROM categories").fetchall()
    conn.close()
    return rows


def add_transaction(t_type):
    """Add a transaction with the given type ('income' or 'expense')."""
    amount = float(input('Amount: '))
    description = input('Description: ')

    # Показываем категории и просим выбрать
    categories = get_categories()
    for cat in categories:
        print(f"{cat[0]}. {cat[1]}")

    category_id = int(input("Choose category number: "))

    # Вставляем данные в таблицу transactions
    conn = get_connection()
    conn.execute(
        "INSERT INTO transactions (amount, type, category_id, description) VALUES (?, ?, ?, ?)",
        (amount, t_type, category_id, description)
    )
    conn.commit()
    conn.close()
    print(f"{t_type.capitalize()} added")


def add_income():
    """Add an income transaction."""
    add_transaction('income')


def add_expense():
    """Add an expense transaction."""
    add_transaction('expense')


def main():
    """Run the main menu loop."""
    while True:
        print("\n=== Finance Tracker ===")
        print("1. Add income")
        print("2. Add expense")
        print("3. Show balance")
        print("4. Show expenses by category")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            show_by_category()
        elif choice == '5':
            print("Good bye!")
            break
        else:
            print("Wrong choice")


if __name__ == '__main__':
    main()