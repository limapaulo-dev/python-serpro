class ContaBancaria():

    def __init__(self, _saldo) -> None:
        self._saldo = _saldo

    def mostrarSaldo(self):
        print(f"Saldo: {self._saldo}")
        print()

    def sacar(self, valor):
        if (self._saldo >= valor):
            self._saldo -= valor
            print(f"Sacado: {valor}")
            self.mostrarSaldo()
        else:
            print(f"Saldo insuficiente para saque no valor de: {valor}")
            self.mostrarSaldo()

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depositado: {valor}")
        self.mostrarSaldo()


conta1 = ContaBancaria(2500)
conta1.mostrarSaldo()

conta1.depositar(500)
conta1.sacar(800)

conta1.sacar(5000)
conta1.sacar(2201)