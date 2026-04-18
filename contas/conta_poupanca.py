from contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero: str, saldo_inicial: float = 0, rendimento: float = 0.005):
        super().__init__(numero, saldo_inicial)
        self._rendimento = rendimento
    
    @property
    def rendimento(self):
        return self._rendimento
    
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("❌ Valor inválido para saque!")
            return False
        
        if valor > self._saldo:
            print(f"❌ Saldo insuficiente! Disponível: R$ {self._saldo:.2f}")
            return False
        
        self._saldo -= valor
        self._historico.adicionar_operacao("SAQUE", valor, self._saldo)
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def aplicar_rendimento(self):
        rendimento_valor = self._saldo * self._rendimento
        self._saldo += rendimento_valor
        self._historico.adicionar_operacao("RENDIMENTO", rendimento_valor, self._saldo)
        print(f"📈 Rendimento de R$ {rendimento_valor:.2f} aplicado!")
