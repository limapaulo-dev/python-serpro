class Student:
    _schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute

class Dude:
    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo

    def introduceSelf(self):
        print(f"Oi! Meu nome é: {self._nome} e tenho {self._idade} anos")


class Hero(Dude):
    def __init__(self, nome, idade, sexo, alterEgo, power):

        super().__init__(nome, idade, sexo)

        self._alterEgo = alterEgo
        self._power = power

    def introduceSelf(self):
        print(f"Eu sou: {self._alterEgo}, e meu poder é {self._power}!")

    def usePower(self):
        print(f"Poder de {self._power}!!!!")

dude1 = Dude("Paulo", 35, "M")
dude2 = Dude("Norberto", 49, "M")
dude3 = Dude("Lucy", 28, "F")

heroDude1 = Hero(dude1._nome, dude1._idade, dude1._sexo, "Homen-Morcego", "Espalhar COVID")

dude1.introduceSelf()
heroDude1.introduceSelf()
heroDude1.usePower()