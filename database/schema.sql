-- SQLite
CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    email TEXT NOT NULL,
    celular TEXT
)