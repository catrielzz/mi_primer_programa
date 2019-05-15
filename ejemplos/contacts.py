ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5


def show_menu():
    print("Acciones Disponibles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return


def add_contact():
    pass


def remove_contact():
    pass


def export_contact():
    pass


def find_contact():
    pass


def main():
    action = show_menu()
    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact()
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact()
        elif action == ACTION_EXPORT_CONTACT:
            export_contact()
        elif action == ACTION_FIND_CONTACT:
            find_contact()
        action = show_menu()


if __name__ == "  main  ":
    main()
