import textwrap

def menuPrincipal():
    menu = """ \n
    Menu Principal
    ==========================

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Conta
    [nu] Novo Usuário
    [q] Sair

    escolhe uma Opção => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito Realizado Com Sucesso")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    while usuario:
        print("Erro.. Já Existe um Usuario Com esse Cpf")
        resp = input("Tentar Outro Cpf (s - sim / n - nao) ")
        if resp == "s":
            cpf = input("Informe o cpf: ")
            usuario = filtrar_usuario(cpf, usuarios)
        else:
            return

    nome = input("Informe o Nome: ")
    data_nasc = input("Informe data de Nscimento (dd-mm-aaaa): ")  
    endereco = input("Informe O endereço: ")
    user = {"nome":nome,"data": data_nasc, "cpf": cpf, "endereco": endereco}
    usuarios.append(user)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    while not usuario:
        print("Erro.. Usuario Não Encontrado")
        resp = input("Tentar Outro Cpf (s - sim / n - nao) ")
        if resp == "s":
            cpf = input("Informe o cpf: ")
            usuario = filtrar_usuario(cpf, usuarios)
        else:
            return

    print("Conta Criada com sucesso!!")
    return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("*" *100)
        print(textwrap.dedent(linha))

def main():

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menuPrincipal()

        if opcao == "d":
            print("\nDepositar Valores")
            print("="*20)
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == "s":
            print("\nSacar Valores")
            print("="*20)
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            s = input("Desejas sair do Programa? (s - sim / n - Não) ")
            if s == "s":
                print("Programa incerrado")
                break
            else:
                continue

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()