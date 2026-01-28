from idlelib.rpc import response_queue
from unittest import case


class Cliente:
    def __init__(self, nome: str, idade : int, documentos :str, saldo : float, diasEstadia :int):
        self.nome = nome
        self.idade = idade
        self.documentos = documentos
        self.saldo = saldo
        self.diasEstadia = diasEstadia
        self.hospedado = False

    def custo_total(self ,preco_diaria):
        return self.diasEstadia * preco_diaria

    def __str__(self):
        status = 'hospedado' if self.hospedado else 'nao hospedado'
        return f'{self.documentos} - {self.nome} - {status}'

class GerenciadorHotel:
    def __init__(self):
        self.listaClientes = [
            Cliente('Arthur', 10,'8123546852', 10000, 6),
            Cliente( 'maria', 26, '9857522256', 3500, 10),
            Cliente('Verona', 36, '98575222565', 3500, 10),

        ]
        self.preco_diaria = 130

    def buscarCliente(self, identificacao, mostrar: bool = False):
        identificacao = str(identificacao).strip().lower()
        resposta = [cliente for cliente in self.listaClientes if cliente.documentos == identificacao]
        if resposta and mostrar: print(resposta[0])
        return resposta [0] if resposta else None

    @staticmethod
    def validarCpfCLiente(documentos):
        return len(documentos) == 11 and documentos.isdigit()

    def criarCliente(self):
        print(f' Criando Cliente...')
        nome = input('Digite o nome do cliente: ')
        idade = int(input('Digite sua idade: '))
        documentos = input(' CPF (somente numeros): ')

        if self.buscarCliente(documentos):
            print('ja exite um cliente com esse documento !')
            return

        if not self.validarCpfCLiente(documentos):
            print('cpf invalido')
            return

        dias = int(input('quantos dias deseja ficar'))
        saldo = float(input('quanto pretende gastar'))
        novoCliente = Cliente(nome, idade, documentos, saldo, dias)
        self.listaClientes.append(novoCliente)
        print('cliente criado com sucesso')

    def listarClientes(self):
        if not self.listaClientes:
            print('Lista Vazia')

        else:
            for cliente in self.listaClientes:
                print(cliente)

    def removerCliente(self,documentos):
        cliente = self.buscarCliente(documentos)
        if cliente:
            self.listaClientes.remove(cliente)
            print('cliente removido com sucesso')
        else:
            print('Cliente nao encontrado')

    def atualizarCliente(self, documentos):
        cliente = self.buscarCliente(documentos)
        if not cliente:
            print('cliente nao encontrada')
        else:
           if cliente.idade < 18:
               print('menor de idade nao pode fazer check in sozinho')
               return
           custo = cliente.custo_total(self.preco_diaria)
           if custo > cliente.saldo:
               print('saldo insuficiente para realizar check in sozinho')
               return
           cliente.hospedado = not cliente.hospedado # esse e o taggle

           acao = 'check in ' if cliente.hospedado else 'check out'
           print(f'{acao} realizado com sucesso')


hotel = GerenciadorHotel()

while True:
    print(f"\n{'='*28}\nSISTEMA GERENCIADOR DE HOTEL\n{'='*28}\n")
    try:
        escolha = int(input('1-Criar | 2-Buscar | 3-lista cliente | 4-Check out | 5-Deletar | 6-Sair :'))
        match escolha:
            case 1: hotel.criarCliente()
            case 2: hotel.buscarCliente(input('Digite o documento do cliente: '), mostrar=True)
            case 3: hotel.listarClientes()
            case 4: hotel.atualizarCliente(input('Digite o documento do cliente: '))
            case 5: hotel.removerCliente(input('Digite o documento do cliente: '))
            case 6: break
            case _: 'opcao invalida'
    except ValueError:
        print('erro, digite apenas numero inteiros')