DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
id INTEGER PRIMARY KEY autoincrement,
titulo STRING NOT NULL,
texto STRING NOT NULL,
data_criacao TIMESTAMP NULL DEFAULT current_timestamp
);