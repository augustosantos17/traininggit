class Paciente:
    def __init__(self, nome):
        self.nome = nome
        self.rg = ""
        self.endereco = ""
        self.telefone = ""
        self.dataNascimento = ""
        self.profissao = ""

    def preencherDados(self, rg, endereco, telefone, dataNascimento, profissao):
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.dataNascimento = dataNascimento
        self.profissao = profissao

    def mostrarDados(self):
        print(f"Nome: {self.nome}")
        print(f"RG: {self.rg}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Data de Nascimento: {self.dataNascimento}")
        print(f"Profissão: {self.profissao}")

# Criação de dois objetos da classe Paciente
paciente1 = Paciente(input("Digite o nome do paciente 1: "))
paciente1.preencherDados(
    input("Digite o RG do paciente 1: "),
    input("Digite o endereço do paciente 1: "),
    input("Digite o telefone do paciente 1: "),
    input("Digite a data de no nascimento do paciente 1: "),
    input("Digite a profissão do paciente 1: ")
)

paciente2 = Paciente(input("\nDigite o nome do paciente 2: "))
paciente2.preencherDados(
    input("Digite o RG do paciente 2: "),
    input("Digite o endereço do paciente 2: "),
    input("Digite o telefone do paciente 2: "),
    input("Digite a data de nascimento do paciente 2: "),
    input("Digite a profissão do paciente 2: ")
)

# Exibição dos dados dos pacientes
print("\nDados do Paciente 1:")
paciente1.mostrarDados()

print("\nDados do Paciente 2:")
paciente2.mostrarDados()
