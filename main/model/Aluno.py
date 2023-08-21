class Aluno():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade
    
    def setNome(self, nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade
    
