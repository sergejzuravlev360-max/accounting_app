import sqlite3

with open('schema.sql', 'r', encoding = 'utr-8') as f:
    schema = f.read()

conn = sqlite3.connect('finance.db')
conn.executescript(schema)
conn.commit()
conn.close()

print('Database created successfully')

def main():
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