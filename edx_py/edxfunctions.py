import curses
import os
import getpass
import hashlib
import subprocess

# Fonction pour changer le nom d'utilisateur
def change_username(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Changer le nom d'utilisateur")
    stdscr.addstr(2, 0, "Entrez le nouveau nom d'utilisateur: ")
    stdscr.refresh()
    new_username = stdscr.getstr(2, 31, 20).decode('utf-8')
    create_or_update_config(new_username, get_username_and_password()[1])
    stdscr.addstr(4, 0, "Nom d'utilisateur mis à jour avec succès.")
    stdscr.refresh()
    stdscr.getch()

# Fonction pour changer le mot de passe
def change_password(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Changer le mot de passe")
    stdscr.addstr(2, 0, "1. Entrez le nouveau mot de passe")
    stdscr.addstr(3, 0, "2. Crypter le mot de passe")
    stdscr.addstr(4, 0, "3. Retour")
    stdscr.refresh()
    
    while True:
        user_input = stdscr.getch()
        if user_input == ord('1'):
            get_and_save_credentials(stdscr)
            break
        elif user_input == ord('2'):
            encrypt_password_with_gnu(stdscr)
            break
        elif user_input == ord('3'):
            break


# Fonction pour créer ou mettre à jour la configuration avec le nom d'utilisateur et le mot de passe
def create_or_update_config(username, password):
    config_path = os.path.expanduser("~/.edx/settings/config.edx")
    config_dir = os.path.dirname(config_path)

    # Crée le répertoire parent s'il n'existe pas
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    with open(config_path, "w") as config_file:
        config_file.write(f"Username: {username}\nPassword: {password}")


# Fonction pour récupérer le nom d'utilisateur et le mot de passe à partir de la configuration
def get_username_and_password():
    if os.path.exists(config_path := os.path.expanduser("~/.edx/settings/config.edx")):
        with open(config_path, "r") as config_file:
            lines = config_file.readlines()
            for line in lines:
                if line.startswith("Username: "):
                    username = line.split(": ")[1].strip()
                elif line.startswith("Password: "):
                    password = line.split(": ")[1].strip()
        return username, password
    return None, None


# Fonction pour demander et enregistrer le nom d'utilisateur et le mot de passe
def get_and_save_credentials(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Saisir le nom d'utilisateur et le mot de passe")

    stdscr.addstr(2, 0, "Nom d'utilisateur: ")
    stdscr.refresh()
    username = stdscr.getstr(2, 18, 20).decode('utf-8')

    stdscr.addstr(4, 0, "Mot de passe: ")
    stdscr.refresh()
    curses.curs_set(1)  # Afficher le curseur pour la saisie du mot de passe
    password = stdscr.getstr(4, 15, 20).decode('utf-8')
    curses.curs_set(0)  # Masquer le curseur après la saisie du mot de passe

    create_or_update_config(username, password)
    stdscr.addstr(6, 0, "Nom d'utilisateur et mot de passe enregistrés.")
    stdscr.refresh()
    stdscr.getch()


# Fonction pour crypter le mot de passe à l'aide des outils GNU
def encrypt_password_with_gnu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Crypter le mot de passe avec des outils GNU")
    stdscr.refresh()

    # Récupérer le mot de passe actuel
    username, password = get_username_and_password()

    # Utiliser openssl pour le cryptage
    try:
        encrypted_password = subprocess.check_output(["openssl", "passwd", "-1", password])
        encrypted_password = encrypted_password.decode('utf-8').strip()
        create_or_update_config(username, encrypted_password)
        stdscr.addstr(2, 0, "Mot de passe crypté avec succès.")
        stdscr.refresh()
    except subprocess.CalledProcessError:
        stdscr.addstr(2, 0, "Erreur lors du cryptage du mot de passe.")
        stdscr.refresh()

    stdscr.getch()


# Fonction pour afficher et gérer les menus de manière récursive
def show_menu(stdscr, menu, depth=0):
    current_option = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, menu["title"])
        options = menu.get("options", [])
        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(i + 2, 0, f"> {option['label']}")
            else:
                stdscr.addstr(i + 2, 0, f"  {option['label']}")
        stdscr.refresh()
        user_input = stdscr.getch()

        if user_input == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif user_input == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif user_input == curses.KEY_RIGHT:
            if "submenu" in options[current_option]:
                show_menu(stdscr, options[current_option]["submenu"], depth + 1)
        elif user_input == 10:  # Touche Entrée
            selected_option = options[current_option]
            action = selected_option.get("action")
            if action:
                action(stdscr)
            elif "submenu" in selected_option:
                show_menu(stdscr, selected_option["submenu"], depth + 1)
            elif selected_option["label"] == "Back" and depth > 0:
                return
        elif user_input == 27:  # Touche Échap pour revenir en arrière
            if depth > 0:
                return


# Fonction pour créer ou mettre à jour la configuration avec le nom d'utilisateur et le mot de passe
def create_or_update_config(username, password):
    config_path = os.path.expanduser("~/.edx/settings/config.edx")
    config_dir = os.path.dirname(config_path)

    # Crée le répertoire parent s'il n'existe pas
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    with open(config_path, "w") as config_file:
        config_file.write(f"Username: {username}\nPassword: {password}")

# Fonction pour récupérer le nom d'utilisateur et le mot de passe à partir de la configuration
def get_username_and_password():
    config_path = os.path.expanduser("~/.edx/settings/config.edx")
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            lines = config_file.readlines()
            for line in lines:
                if line.startswith("Username: "):
                    username = line.split(": ")[1].strip()
                elif line.startswith("Password: "):
                    password = line.split(": ")[1].strip()
        return username, password
    return None, None

# Fonction pour demander le nom d'utilisateur et le mot de passe à l'utilisateur
def get_user_input(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Saisir le nom d'utilisateur et le mot de passe")
    
    stdscr.addstr(2, 0, "Nom d'utilisateur: ")
    stdscr.refresh()
    username = stdscr.getstr(2, 18, 20).decode('utf-8')

    stdscr.addstr(4, 0, "Mot de passe: ")
    stdscr.refresh()
    curses.curs_set(1)  # Afficher le curseur pour la saisie du mot de passe
    password = stdscr.getstr(4, 15, 20).decode('utf-8')
    curses.curs_set(0)  # Masquer le curseur après la saisie du mot de passe

    return username, password

# Fonction pour vérifier le nom d'utilisateur et le mot de passe
def check_credentials(username, password):
    saved_username, saved_password = get_username_and_password()
    return username == saved_username and password == saved_password

# Fonction pour crypter le mot de passe à l'aide des outils GNU
def encrypt_password_with_gnu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Crypter le mot de passe avec des outils GNU")
    stdscr.refresh()

    # Récupérer le mot de passe actuel
    username, password = get_username_and_password()

    # Utiliser openssl pour le cryptage
    try:
        encrypted_password = subprocess.check_output(["openssl", "passwd", "-1", password])
        encrypted_password = encrypted_password.decode('utf-8').strip()
        create_or_update_config(username, encrypted_password)
        stdscr.addstr(2, 0, "Mot de passe crypté avec succès.")
        stdscr.refresh()
    except subprocess.CalledProcessError:
        stdscr.addstr(2, 0, "Erreur lors du cryptage du mot de passe.")
        stdscr.refresh()

    stdscr.getch()
    


def show_help():
    print("show config.txt")


def usr_crack_function():
    print("show config.txt")
    

def show_files():
    print("show config.txt")
    


def list_and_execute_commands(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Liste des commandes du PATH")
    stdscr.refresh()

    # Récupérer les commandes du PATH
    path_dirs = os.environ['PATH'].split(os.pathsep)
    commands = []
    for path_dir in path_dirs:
        if os.path.isdir(path_dir):
            commands.extend([f for f in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, f))])

    # Divisez la liste des commandes en pages pour la pagination
    page_size = curses.LINES - 4  # Nombre de lignes affichées par page
    command_pages = [commands[i:i + page_size] for i in range(0, len(commands), page_size)]
    current_page = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Liste des commandes du PATH (Page {} de {})".format(current_page + 1, len(command_pages)))
        commands_to_display = command_pages[current_page]

        for i, option in enumerate(commands_to_display):
            if i == current_option:
                stdscr.addstr(i + 2, 0, option, curses.A_STANDOUT)
            else:
                stdscr.addstr(i + 2, 0, option)

        stdscr.refresh()
        user_input = stdscr.getch()

        if user_input == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif user_input == curses.KEY_DOWN and current_option < len(commands_to_display) - 1:
            current_option += 1
        elif user_input == 10:  # Touche Entrée
            selected_option = commands_to_display[current_option]
            if selected_option:
                # Exécuter la commande dans une nouvelle fenêtre de terminal
                os.system(selected_option)
                stdscr.refresh()
                stdscr.getch()
        elif user_input == ord('q') or user_input == ord('Q'):
            break
