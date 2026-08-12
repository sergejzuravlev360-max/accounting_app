CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL CHECK (amount > 0),
    type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
    category_id INTEGER NOT NULL,
    description TEXT,
    date TEXT NOT NULL DEFAULT (date('now')),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
INSERT INTO categories (name) VALUES ('Еда');
INSERT INTO categories (name) VALUES ('Транспорт');
INSERT INTO categories (name) VALUES ('Зарплата');

INSERT INTO transactions (amount, type, category_id, description)
VALUES (150.50, 'expense', 1, 'Обед в кафе');

INSERT INTO transactions (amount, type, category_id, description)
VALUES (50000, 'income', 3, 'Зарплата за август');
