from datetime import datetime

class Historico:
    def __init__(self):
        self._operacoes = []  # Composição
    
    def adicionar_operacao(self, tipo: str, valor: float, saldo_apos: float):
        operacao = {
            "tipo": tipo,
            "valor": valor,
            "saldo_apos": saldo_apos,
            "data": datetime.now()
        }
        self._operacoes.append(operacao)
    
    def listar_operacoes(self):
        if not self._operacoes:
            print("\n📭 Nenhuma operação realizada ainda!")
            return
        
        print("\n" + "="*60)
        print("📋 HISTÓRICO DE OPERAÇÕES")
        print("="*60)
        for i, op in enumerate(self._operacoes, 1):
            print(f"{i}. [{op['data'].strftime('%d/%m/%Y %H:%M:%S')}]")
            print(f"   Tipo: {op['tipo']}")
            print(f"   Valor: R$ {op['valor']:.2f}")
            print(f"   Saldo após: R$ {op['saldo_apos']:.2f}")
            print("-"*40)
    
    def get_operacoes(self):
        return self._operacoes
