# agenda.py

class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def listar_contatos(self):
        for i, contato in enumerate(self.contatos):
            favorito = "Sim" if contato.favorito else "Não"
            print(f"{i+1}. {contato.nome} - {contato.telefone} - {contato.email} - Favorito: {favorito}")
    
    def editar_contato(self, index, novo_contato):
        self.contatos[index] = novo_contato
    
    def marcar_como_favorito(self, index):
        self.contatos[index].favorito = True
    
    def desmarcar_como_favorito(self, index):
        self.contatos[index].favorito = False
    
    def listar_favoritos(self):
        favoritos = [c for c in self.contatos if c.favorito]
        for i, contato in enumerate(favoritos):
            print(f"{i+1}. {contato.nome} - {contato.telefone} - {contato.email}")
    
    def apagar_contato(self, index):
        self.contatos.pop(index)

def menu():
    print("\n=== Menu Agenda ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Listar contatos favoritos")
    print("7. Apagar contato")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    agenda = Agenda()
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        
        elif opcao == '2':
            agenda.listar_contatos()
        
        elif opcao == '3':
            agenda.listar_contatos()
            index = int(input("Digite o número do contato a editar: ")) - 1
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, email)
            agenda.editar_contato(index, contato)
        
        elif opcao == '4':
            agenda.listar_contatos()
            index = int(input("Digite o número do contato a marcar como favorito: ")) - 1
            agenda.marcar_como_favorito(index)
        
        elif opcao == '5':
            agenda.listar_contatos()
            index = int(input("Digite o número do contato a desmarcar como favorito: ")) - 1
            agenda.desmarcar_como_favorito(index)
        
        elif opcao == '6':
            agenda.listar_favoritos()
        
        elif opcao == '7':
            agenda.listar_contatos()
            index = int(input("Digite o número do contato a apagar: ")) - 1
            agenda.apagar_contato(index)
        
        elif opcao == '0':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()