
class Pessoa :
    def __init__(self,cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, valor):

        valor = valor.replace(".","").replace("-","")

        if not valor.isdigit():
            raise ValueError("CPF deve conter apenas numeros")
        
        if len(valor) != 11:
            raise ValueError("CPF deve conter 11 digitos")
        
        self._cpf = valor


p1 = Pessoa("12345607901")
print(p1.cpf)  # Saída: 12345678901

p2 = Pessoa("12345678902")  # Levanta ValueError: CPF deve conter apenas dígito
print(p2.cpf)