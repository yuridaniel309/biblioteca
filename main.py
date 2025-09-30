import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros(
     id INTEGER PRIMARY KEY AUTOINCREMENT"0
      titul TEXT)
      autor TEXT NOT NULL
      ano INTEGER
      disponivel CHAR(3) CHECK(disponivel IN ("SIM","Nao"))
      )
""")

#inserir um  livro no banco de dados
nome = input("digite o nome do livro que deseja cadastrar:")
cursor.execute("""
INSERT INTO livro (titulo,autro,ano)
VALUES(?,?,?)
          
""",)
conexao.execute()

def cadastrar_livro(titulo,autor,ano):
  nome = input("digite o nome livro que deseja cadastrar:")
  cursor.execute("""
INSERT INTO livros (titulo,autro,ano)
VALUES (?,?,?)
  )
               
               
               
               
               
               
               
               
               
               """)