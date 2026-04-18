from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero: str, saldo_inicial: float = 0, limite: float = 500):
        super().__init__(numero, saldo_inicial)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("❌ Valor inválido para saque!")
            return False
        
        saldo_disponivel = self._saldo + self._limite
        
        if valor > saldo_disponivel:
            print(f"❌ Saldo + limite insuficiente! Disponível: R$ {saldo_disponivel:.2f}")
            return False
        
        self._saldo -= valor
        self._historico.adicionar_operacao("SAQUE", valor, self._saldo)
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def consultar_saldo(self):
        print(f"\n💰 Saldo Conta Corrente: R$ {self._saldo:.2f}")
        print(f"💳 Limite disponível: R$ {self._limite:.2f}")
        print(f"📊 Total disponível: R$ {(self._saldo + self._limite):.2f}")
        return self._saldo
