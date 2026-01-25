
class Pessoa:
    def __init__(self, idade):
        self.idade = idade


    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor


P1 = Pessoa(25)
print(P1.idade)  # Saída: 25

P2 = Pessoa(45)  # Levanta ValueError: Idade não pode ser negativa
print(P2.idade) 

P3 = Pessoa(30)
print(P3.idade)  # Saída: 30



class Pessoa :
    @property
    def idade(self):
        return self.__idade 
    
p = Pessoa('joselina', idade=30)
print(p.idade)  # Levanta AttributeError: 'Pessoa' object has no attribute '_Pessoa__idade'

class Pessoa :
    def __init__(self):
        self.idade = 0

    def set_idade(self, valor):
        if valor >= 0:
            self.__idade = valor
        else:
            print('idade invalida')

    def get_idade(self):
        return self.__idade
p = Pessoa()
p.set_idade(-25)



class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.ver_saldo())  # Saída: 1500

conta1 = ContaBancaria(2000)
conta1.depositar(300)   
print(conta1.ver_saldo())  # Saída: 2300
 

class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late")


a = Animal()

C = Cachorro()


a.falar()  # Saída: O animal faz um som
C.falar()  # Saída: O cachorro late

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("que som faz o animal faz um som.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)   # chama o __init__ da classe pai
        self.raca = raca

    def falar(self):
        super().falar()         # chama o método da classe pai
        print("O cachorro late!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)   # chama o __init__ da classe pai
        self.cor = cor

    def falar(self):
        super().falar()         # chama o método da classe pai
        print("O gato mia!")

cachorro = Cachorro("Rex", "Labrador")
cachorro.falar()


gato = Gato("Mimi", "Branco")
gato.falar()
class Pessoa:
    def __init__(self, idade):
        self.idade = idade


    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor


P1 = Pessoa(25)
print(P1.idade)  # Saída: 25

P2 = Pessoa(45)  # Levanta ValueError: Idade não pode ser negativa
print(P2.idade) 

P3 = Pessoa(30)
print(P3.idade)  # Saída: 30



class Pessoa :
    @property
    def idade(self):
        return self.__idade 
    
p = Pessoa('joselina', idade=30)
print(p.idade)  # Levanta AttributeError: 'Pessoa' object has no attribute '_Pessoa__idade'

class Pessoa :
    def __init__(self):
        self.idade = 0

    def set_idade(self, valor):
        if valor >= 0:
            self.__idade = valor
        else:
            print('idade invalida')

    def get_idade(self):
        return self.__idade
p = Pessoa()
p.set_idade(-25)



class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.ver_saldo())  # Saída: 1500

conta1 = ContaBancaria(2000)
conta1.depositar(300)   
print(conta1.ver_saldo())  # Saída: 2300
 

class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late")


a = Animal()

C = Cachorro()


a.falar()  # Saída: O animal faz um som
C.falar()  # Saída: O cachorro late

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("que som faz o animal faz um som.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)   # chama o __init__ da classe pai
        self.raca = raca

    def falar(self):
        super().falar()         # chama o método da classe pai
        print("O cachorro late!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)   # chama o __init__ da classe pai
        self.cor = cor

    def falar(self):
        super().falar()         # chama o método da classe pai
        print("O gato mia!")

cachorro = Cachorro("Rex", "Labrador")
cachorro.falar()


gato = Gato("Mimi", "Branco")
gato.falar()




class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veículo está ligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def ligar(self):
        super().ligar()
        print("O carro está pronto para dirigir.")

    def buzinar(self):
        print("Buzina do carro: Beep Beep!")


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def ligar(self):
        super().ligar()
        print("A moto está pronta para pilotar.")

    def buzinar(self):
        print("Buzina da moto: Meep Meep!")

        
carro = Carro("Toyota", "Corolla", 4)
carro.ligar()
carro.buzinar()


ve = Carro('Ford', 'Fiesta', 4)
ve.ligar()
ve.buzinar()

ioto = Moto('Honda', 'CB500', 'Esportiva')
ioto.ligar()
ioto.buzinar()  # Levanta AttributeError: 'Veiculo' object has no attribute 'buzinar'


class Pessoa :
    def __init__(self,nome):
        self.nome = nome
    def apresentar(self):
        print(f"Ola, meu nome e {self.nome}.")


p = Pessoa("Joao")
p.apresentar()  # Saída: Olá, meu nome é João.

p1 = Pessoa("Maria")
p1.apresentar()  # Saída: Olá, meu nome é Maria.

p2 = Pessoa("Ayrton")
p2.apresentar()  # Saída: Olá, meu nome é Ayrton.

p3 = Pessoa('verona')
p3.apresentar()  # Saída: Olá, meu nome é Verona.

p4 = Pessoa('Arthur Benicio')
p4.apresentar()  # Saída: Olá, meu nome é Arthur Benicio.



class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(self.saldo)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


conta = Conta(1000)
conta.depositar(500)    
conta.mostrar_saldo()  # Saída: 1500

c1 = Conta(2000)
c1.sacar(2500)         # Saída: Saldo insuficiente

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veículo está ligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def ligar(self):
        super().ligar()
        print("O carro está pronto para dirigir.")

    def buzinar(self):
        print("Buzina do carro: Beep Beep!")


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def ligar(self):
        super().ligar()
        print("A moto está pronta para pilotar.")

    def buzinar(self):
        print("Buzina da moto: Meep Meep!")

        
carro = Carro("Toyota", "Corolla", 4)
carro.ligar()
carro.buzinar()


ve = Carro('Ford', 'Fiesta', 4)
ve.ligar()
ve.buzinar()

ioto = Moto('Honda', 'CB500', 'Esportiva')
ioto.ligar()
ioto.buzinar()  # Levanta AttributeError: 'Veiculo' object has no attribute 'buzinar'


class Pessoa :
    def __init__(self,nome):
        self.nome = nome
    def apresentar(self):
        print(f"Ola, meu nome e {self.nome}.")


p = Pessoa("Joao")
p.apresentar()  # Saída: Olá, meu nome é João.

p1 = Pessoa("Maria")
p1.apresentar()  # Saída: Olá, meu nome é Maria.

p2 = Pessoa("Ayrton")
p2.apresentar()  # Saída: Olá, meu nome é Ayrton.

p3 = Pessoa('verona')
p3.apresentar()  # Saída: Olá, meu nome é Verona.

p4 = Pessoa('Arthur Benicio')
p4.apresentar()  # Saída: Olá, meu nome é Arthur Benicio.



class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(self.saldo)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


conta = Conta(1000)
conta.depositar(500)    
conta.mostrar_saldo()  # Saída: 1500

c1 = Conta(2000)
c1.sacar(2500)         # Saída: Saldo insuficiente






class Carro:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

c1 = Carro("Toyota", "Corolla" , 120000)
c2 = Carro("Honda", "Civic" , 130000)

print(c1.marca,c1.preco,c1.modelo)   # Saída: Toyota 120000 Corolla
print(c2.modelo, c2.preco, c2.modelo)  # Saída: Civic 130000

class Carro:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

c1 = Carro("Toyota", "Corolla" , 120000)
c2 = Carro("Honda", "Civic" , 130000)

print(c1.marca,c1.preco,c1.modelo)   # Saída: Toyota 120000 Corolla
print(c2.modelo, c2.preco, c2.modelo)  # Saída: Civic 130000


class Casa:
    def __init__(self,cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

c1 = Casa("Azul", 120)
c2 = Casa("Vermelha", 150)

print(c1.cor, c1.tamanho)      # Saída: Azul 120
print(c2.cor, c2.tamanho)      # Saída: Vermelha 150    