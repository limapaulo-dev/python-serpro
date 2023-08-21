from .DAO import DAO

class AlunoDAO(DAO):
    _dbTableName = "aluno"

    def __init__(self, conn):
        DAO.__init__(self, conn)

    def insertAluno(self, aluno):
        self._conn.execute(f"INSERT INTO {self._dbTableName} (nome, idade) VALUES (?, ?)", (aluno.getNome(), aluno.getIdade()))
        self._conn.commit()
        print(f"Aluno(a) {aluno.getNome()}, inserido(a) com sucesso.")

    def updateById(self, aluno, id):
        self._conn.execute(f"UPDATE {self._dbTableName} SET nome=?, idade=? WHERE id = ?", (aluno.getNome(), aluno.getIdade(), id))
        self._conn.commit()
        print(f"Aluno(a) {aluno.getNome()}, atualizado(a) com sucesso.")

    
