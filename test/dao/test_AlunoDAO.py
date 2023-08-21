import unittest
import sqlite3
from main.dao.AlunoDAO import AlunoDAO
from main.model.Aluno import Aluno

class testAluno(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''
         CREATE TABLE IF NOT EXISTS aluno 
         (
         id INTEGER PRIMARY KEY,
         nome VARCHAR(255) NOT NULL,
         idade INTEGER NOT NULL
         )            
         ''')
        alunoSpected1 = Aluno("Paulo Lima", 35)
        alunoSpected2 = Aluno("Luke Skywalker", 45) 
        alunoDAO = AlunoDAO(self.conn)
        alunoDAO.insertAluno(alunoSpected1)
        alunoDAO.insertAluno(alunoSpected2)

    def tearDown(self):
        self.conn.close()
    
    def test_insertAlunoPNome(self):   
        aluno1Spected = "Paulo Lima"
        alunoDAO = AlunoDAO(self.conn)
        alunoActual = alunoDAO.selectAll().fetchall()
        self.assertIn(aluno1Spected, alunoActual[0])

    def test_insertAlunoPIdade(self):   
        aluno1Spected = 45
        alunoDAO = AlunoDAO(self.conn)
        alunoActual = alunoDAO.selectAll().fetchall()
        self.assertIn(aluno1Spected, alunoActual[1])

    def test_selectAllPLen(self):
        spectedLen = 2
        alunoDAO = AlunoDAO(self.conn)
        actualLen = len(alunoDAO.selectAll().fetchall())
        self.assertEqual(spectedLen, actualLen)

    def test_selectByID(self):
        spectedID1 = 1
        alunoDAO = AlunoDAO(self.conn)
        actualID1 = alunoDAO.selectById(1).fetchall()
        self.assertEqual(spectedID1, actualID1[0][0])

    def test_deleteById(self):
        spectedLen = 1
        alunoDAO = AlunoDAO(self.conn)
        alunoDAO.deleteById(1)
        actualLen = len(alunoDAO.selectAll().fetchall())
        self.assertEqual(spectedLen, actualLen)



