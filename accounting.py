import sqlite3

# Читаем SQL-схему из файла
with open('schema.sql', 'r', encoding='utf-8') as f:
    schema = f.read()

# Открываем базу и выполняем схему
conn = sqlite3.connect('finance.db')
conn.executescript(schema)
conn.commit()
conn.close()

print('Database created successfully')


# Подключение к базе
def get_connection():
    return sqlite3.connect('finance.db')


# Получить все категории
def get_categories():
    conn = get_connection()
    rows = conn.execute("SELECT id, name FROM categories").fetchall()
    conn.close()
    return rows


# Добавить операцию (доход или расход)
def add_transaction(t_type):
    amount = float(input('Amount: '))
    description = input('Description: ')

    # Показываем категории
    categories = get_categories()
    for cat in categories:
        print(f"{cat[0]}. {cat[1]}")

    category_id = int(input("Category number: "))

    # Записываем в базу
    conn = get_connection()
    conn.execute(
        "INSERT INTO transactions (amount, type, category_id, description) VALUES (?, ?, ?, ?)",
        (amount, t_type, category_id, description)
    )
    conn.commit()
    conn.close()
    print(f"{t_type.capitalize()} added")


# Добавить доход
def add_income():
    add_transaction('income')


# Добавить расход
def add_expense():
    add_transaction('expense')


# Показать баланс
def show_balance():
    conn = get_connection()
    result = conn.execute("""
        SELECT
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) -
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS balance
        FROM transactions
    """).fetchone()
    conn.close()
    print(f"Balance: {result[0]}")


# Показать расходы по категориям
def show_by_category():
    conn = get_connection()
    rows = conn.execute("""
        SELECT c.name, SUM(t.amount) AS total
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.type = 'expense'
        GROUP BY c.name
    """).fetchall()
    conn.close()

    print("\nExpenses by category:")
    for row in rows:
        print(f"{row[0]}: {row[1]}")


# Главное меню
def main():
    while True:
        print("\nFinance Tracker")
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