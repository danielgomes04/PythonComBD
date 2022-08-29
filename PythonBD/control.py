from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n" +
              "0. Sair\n"                             +
              "1. Cadastrar\n"                     +
              "2. Consultar\n"                     +
              "3. Atualizar\n"                     +
              "4. Excluir")
        self.setOpcao(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            else:
                print("Opção escolhida não é válida.")

    def transformarData(self, texto):
        separado = texto.split('/')#separa em vetores as partes com / que o usuario digitou
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano,mes,dia)

    def cadastrar(self):
        print("Informe o seu nome: ")
        nome = input()
        print("Informe seu telefone: ")
        telefone = input()
        print("Informe o seu endereço: ")
        endereco = input()
        print("Informe a sua data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome,telefone,endereco, self.transformarData(dataDeNascimento)))