class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite


class Agenda:
    def __init__(self):
        self.contacts = []

    def edit_contact(self, index, contact):
        if index >= 0 and index < len(self.contacts):
            self.contacts[index] = contact
        else:
            print("Invalid index!")

    def delete_contact(self, index):
        if index >= 0 and index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid index!")

    def mark_favorite(self, index):
        if index >= 0 and index < len(self.contacts):
            self.contacts[index].favorite = True
        else:
            print("Invalid index!")

    def unmark_favorite(self, index):
        if index >= 0 and index < len(self.contacts):
            self.contacts[index].favorite = False
        else:
            print("Invalid index!")

    def get_all_contacts(self):
        return self.contacts

    def get_favorite_contacts(self):
        return [contact for contact in self.contacts if contact.favorite]


# Exemplo de uso
agenda = Agenda()
while True:
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Deletar Contato")
    print("4. Marcar/Desmarcar como Favorito")
    print("5. Ver Todos os Contatos")
    print("6. Ver Contatos Favoritos")
    print("0. Sair")
    choice = input("Digite sua escolha: ")
    if choice == "1":
        name = input("Digite o nome: ")
        phone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        favorite = input("Esse contato é um favorito? (s/n): ").lower() == "s"
        contact = Contact(name, phone, email, favorite)
        agenda.add_contact(contact)
        print("Contato adicionado com sucesso!")
    elif choice == "2":
        index = int(input("Digite o índice do contato a ser editado: "))
        name = input("Digite o novo nome: ")
        phone = input("Digite o novo telefone: ")
        email = input("Digite o novo email: ")
        favorite = input("Esse contato é um favorito? (s/n): ").lower() == "s"
        contact = Contact(name, phone, email, favorite)
        agenda.edit_contact(index, contact)
        print("Contato editado com sucesso!")
    elif choice == "3":
        index = int(input("Digite o índice do contato a ser deletado: "))
        agenda.delete_contact(index)
        print("Contato deletado com sucesso!")
    elif choice == "4":
        index = int(
            input("Digite o índice do contato para marcar/desmarcar como favorito: ")
        )
        contact = agenda.get_all_contacts()[index]
        if contact.favorite:
            agenda.unmark_favorite(index)
            print("Contato desmarcado como favorito!")
        else:
            agenda.mark_favorite(index)
            print("Contato marcado como favorito!")
    elif choice == "5":
        contacts = agenda.get_all_contacts()
        for i, contact in enumerate(contacts):
            print(
                f"{i}. {contact.name} - {contact.phone} - {contact.email} - Favorito: {contact.favorite}"
            )
    elif choice == "6":
        favorite_contacts = agenda.get_favorite_contacts()
        for i, contact in enumerate(favorite_contacts):
            print(f"{i}. {contact.name} - {contact.phone} - {contact.email}")
    elif choice == "0":
        break
    else:
        print("Escolha inválida. Por favor, tente novamente.")
