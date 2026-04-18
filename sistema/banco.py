from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from clientes.cliente import Cliente

class Banco:
    def __init__(self, nome: str):
        self._nome = nome
        self._contas = {}  # Agregação: dicionário de contas
        self._clientes = {}  # Agregação: dicionário de clientes
    
    def criar_conta(self, tipo: str, numero: str, saldo_inicial: float, cliente_cpf: str):
        if numero in self._contas:
            print("❌ Número de conta já existe!")
            return None
        
        if cliente_cpf not in self._clientes:
            print("❌ Cliente não encontrado! Cadastre o cliente primeiro.")
            return None
        
        if tipo == "corrente":
            conta = ContaCorrente(numero, saldo_inicial)
        elif tipo == "poupanca":
            conta = ContaPoupanca(numero, saldo_inicial)
        else:
            print("❌ Tipo de conta inválido!")
            return None
        
        self._contas[numero] = conta
        cliente = self._clientes[cliente_cpf]
        cliente.adicionar_conta(conta)
        print(f"✅ Conta {tipo} {numero} criada com sucesso!")
        return conta
    
    def cadastrar_cliente(self, nome: str, cpf: str, endereco: str = ""):
        if cpf in self._clientes:
            print("❌ Cliente já cadastrado!")
            return None
        
        cliente = Cliente(nome, cpf, endereco)
        self._clientes[cpf] = cliente
        print(f"✅ Cliente {nome} cadastrado com sucesso!")
        return cliente
    
    def get_conta(self, numero: str):
        return self._contas.get(numero)
    
    def get_cliente(self, cpf: str):
        return self._clientes.get(cpf)
    
    def listar_contas(self):
        if not self._contas:
            print("📭 Nenhuma conta cadastrada!")
            return
        
        print("\n" + "="*50)
        print("🏦 CONTAS CADASTRADAS")
        print("="*50)
        for numero, conta in self._contas.items():
            print(f"Conta: {numero} | Saldo: R$ {conta.saldo:.2f}")
