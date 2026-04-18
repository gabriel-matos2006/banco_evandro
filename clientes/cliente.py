class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str = ""):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._contas = []  # Agregação
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def contas(self):
        return self._contas
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print(f"✅ Conta {conta.numero} vinculada ao cliente {self._nome}")
    
    def remover_conta(self, numero_conta):
        self._contas = [c for c in self._contas if c.numero != numero_conta]
