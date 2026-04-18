from abc import ABC, abstractmethod
from operacoes.historico import Historico

class Conta(ABC):
    def __init__(self, numero: str, saldo_inicial: float = 0):
        self._numero = numero
        self._saldo = saldo_inicial
        self._historico = Historico()  # Composição
        self._ativa = True
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historico(self):
        return self._historico
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        """Método abstrato - polimorfismo"""
        pass
    
    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("❌ Valor inválido para depósito!")
            return False
        
        self._saldo += valor
        self._historico.adicionar_operacao("DEPÓSITO", valor, self._saldo)
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def consultar_saldo(self):
        print(f"\n💰 Saldo atual: R$ {self._saldo:.2f}")
        return self._saldo
    
    def desativar(self):
        self._ativa = False
    
    def esta_ativa(self):
        return self._ativa
