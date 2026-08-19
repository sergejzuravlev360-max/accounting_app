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

SELECT c.name, SUM(t.amount) AS total
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.type = 'expense'
GROUP BY c.name;

SELECT
    SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) -
    SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS balance
FROM transactions;

SELECT t.id, c.name AS category, t.type, t.amount, t.description, t.date
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE strftime('%Y-%m', t.date) = strftime('%Y-%m', 'now')
ORDER BY t.date DESC;

-- Средний чек по расходам
SELECT c.name, AVG(t.amount) AS avg_expense
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.type = 'expense'
GROUP BY c.name;

-- Количество операций по категориям
SELECT c.name, COUNT(t.id) AS operations_count
FROM transactions t
JOIN categories c ON t.category_id = c.id
GROUP BY c.name
ORDER BY operations_count DESC;

SELECT c.name, MAX(t.amount) AS max_expense
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.type = 'expense'
GROUP BY c.name;

SELECT c.name,
       SUM(CASE WHEN t.type = 'income' THEN t.amount ELSE 0 END) AS total_income,
       SUM(CASE WHEN t.type = 'expense' THEN t.amount ELSE 0 END) AS total_expense
FROM transactions t
JOIN categories c ON t.category_id = c.id
GROUP BY c.name;

SELECT c.name, SUM(t.amount) AS total_expense
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.type = 'expense'
GROUP BY c.name
ORDER BY total_expense DESC
LIMIT 1;