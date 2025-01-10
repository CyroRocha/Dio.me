def sacar(self, valor:float) -> None:
    saldo = 500
    
    if self.saldo >= valor:
        print("valor sacado")
        self.saldo -= valor


sacar(100)