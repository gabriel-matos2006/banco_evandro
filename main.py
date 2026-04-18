from sistema.banco import Banco

def exibir_menu():
    print("\n" + "="*50)
    print("🏧 SISTEMA DE CAIXA ELETRÔNICO 🏧")
    print("="*50)
    print("1️⃣  - Criar Cliente")
    print("2️⃣  - Criar Conta")
    print("3️⃣  - Depositar")
    print("4️⃣  - Sacar")
    print("5️⃣  - Consultar Saldo")
    print("6️⃣  - Ver Histórico")
    print("7️⃣  - Listar Contas")
    print("0️⃣  - Sair")
    print("="*50)

def main():
    banco = Banco("Banco POO")
    
    while True:
        exibir_menu()
        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF: ")
            endereco = input("Endereço (opcional): ")
            banco.cadastrar_cliente(nome, cpf, endereco)
        
        elif opcao == "2":
            cpf = input("CPF do cliente: ")
            if not banco.get_cliente(cpf):
                print("❌ Cliente não encontrado! Cadastre o cliente primeiro.")
                continue
            
            tipo = input("Tipo da conta (corrente/poupanca): ").lower()
            numero = input("Número da conta: ")
            saldo = float(input("Saldo inicial: R$ "))
            banco.criar_conta(tipo, numero, saldo, cpf)
        
        elif opcao == "3":
            numero = input("Número da conta: ")
            conta = banco.get_conta(numero)
            if conta:
                valor = float(input("Valor para depósito: R$ "))
                conta.depositar(valor)
            else:
                print("❌ Conta não encontrada!")
        
        elif opcao == "4":
            numero = input("Número da conta: ")
            conta = banco.get_conta(numero)
            if conta:
                valor = float(input("Valor para saque: R$ "))
                conta.sacar(valor)
            else:
                print("❌ Conta não encontrada!")
        
        elif opcao == "5":
            numero = input("Número da conta: ")
            conta = banco.get_conta(numero)
            if conta:
                conta.consultar_saldo()
            else:
                print("❌ Conta não encontrada!")
        
        elif opcao == "6":
            numero = input("Número da conta: ")
            conta = banco.get_conta(numero)
            if conta:
                conta.historico.listar_operacoes()
            else:
                print("❌ Conta não encontrada!")
        
        elif opcao == "7":
            banco.listar_contas()
        
        elif opcao == "0":
            print("\n👋 Obrigado por usar nosso sistema! Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
