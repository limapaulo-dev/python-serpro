import sqlite3
from dao.DAO import DAO
from dao.AlunoDAO import AlunoDAO
from model.Aluno import Aluno


dbName = "sqlite3"
conn = None

try:
    conn = sqlite3.connect(dbName)

    print(f"sqlite DB:'{dbName}' connected")

    try:
        conn.execute('''
                DROP TABLE aluno            
                ''')
    except sqlite3.Error as e:
        print(f"DROP TABLE error: {e}")

    conn.execute('''
            CREATE TABLE IF NOT EXISTS aluno 
            (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            idade INTEGER NOT NULL
            )            
            ''')

    dao = DAO(conn)

    alunoDAO = AlunoDAO(conn)

    aluno1 = Aluno("Walter White", 50)
    aluno2 = Aluno("Jessie Pinkman", 24)
    aluno3 = Aluno("Jack Sparrow", 39)
    aluno4 = Aluno("John Locke", 52)
    aluno5 = Aluno("Scooby Doo", 8)
    aluno6 = Aluno("Luke Skywalker", 27)
    aluno7 = Aluno("Black Tom", 35)
    aluno8 = Aluno("Charles Thomas Tester", 20)
    aluno9 = Aluno("Some dude", 74)
    aluno10 = Aluno("Last dude", 44)

    alunoDAO.insertAluno(aluno1)
    alunoDAO.insertAluno(aluno2)
    alunoDAO.insertAluno(aluno3)
    alunoDAO.insertAluno(aluno4)
    alunoDAO.insertAluno(aluno5)
    alunoDAO.insertAluno(aluno6)
    alunoDAO.insertAluno(aluno7)
    alunoDAO.insertAluno(aluno8)
    alunoDAO.insertAluno(aluno9)
    alunoDAO.insertAluno(aluno10)
    alunoDAO.deleteById(5)
    alunoDAO.deleteById(25)

    aluno9.setNome("Charles Manson")
    aluno9.setIdade(65)
    alunoDAO.updateById(aluno9, 9)

    resultAlunos = alunoDAO.selectAll()
    listaAlunos = resultAlunos.fetchall()

    tabelaTitulos = tuple(map(lambda x : x[0], resultAlunos.description))

    print(resultAlunos)
    print(tabelaTitulos)
    print(listaAlunos)

    for aluno in listaAlunos:
        print(aluno)

except sqlite3.Error as e:
    print(e)

finally:
    if conn:
        conn.close()
        print("sqlite connection closed")
