import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT,
autor TEXT NOT NULL,
ano INTEGER
)            
""")

cursor.execute
#inserir um  livro no banco de dados
nome = input("digite o nome do livro que deseja cadastrar:")
cursor.execute("""
INSERT INTO livros (titulo,autor,ano)
VALUES(?,?,?)
          
""",)


def cadastrar_livro(titulo,autor,ano):
  cursor.execute()
nome = input("digite o nome livro que deseja cadastrar:")
cursor.execute("""
INSERT INTO livros (titulo,autro,ano)
VALUES (?,?,?)
)
                      
""")          
#mostrando os livro cadastrados
def mostra_livro():
    cursor.execute("SELECT * FROM livros")
    for linha in cursor. fetchall():
      print(f"ID:{linha[0]} TITULO:{linha[1]} AUTOR: {linha[2]} ANO:{linha[3]} DISPONIBILIDADE:{linha[4]}")        
conexao.close()

 
#atualização de disponibilidade
def atualizar_livros():
    id = int(input("digite o id do livro que deseja pegar: "))
    while True: 
        disponivel = input("Deixar disponivel ou não (sim ou não): ").lower()
        if disponivel == "sim" or disponivel == "não":
            break
        else:
            print("Digite apenas sim ou não para deixar disponivel.")
    cursor.execute("""
    UPDATE livros
    SET disponivel = ? 
    WHERE id = ?
    """, (disponivel,id)
    )
    