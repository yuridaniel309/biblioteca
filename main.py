import sqlite3

conexão = sqlite3.connect("biblioteca.db")
cursor = conexão.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros(
     id INTEGER PRIMARY KEY AUTOINCREMENT"0
      titul TEXT)
      autor TEXT NOT NULL
      ano INTEGER
      disponivel CHAR(3) CHECK(disponivel IN ("SIM","Não"))
      )
""")

#inserir um  livro no banco de dados
nome = input("digite o nome do livro que deseja cadastrar:")
cursor.execute("""
INSERT INTO livro (titulo,autro,ano)
VALUES(?,?,?)
""",)
