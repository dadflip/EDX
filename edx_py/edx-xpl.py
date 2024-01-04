import curses
import os
import getpass
import hashlib
import subprocess

from edxfunctions import *


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    sh, sw = stdscr.getmaxyx()

    title = "Main Menu - Press ENTER\n"
    stdscr.addstr(0, sw // 2 - len(title) // 2, title)

    # Demander le nom d'utilisateur et le mot de passe à l'utilisateur
    username, password = get_user_input(stdscr)

    # Vérifier les informations d'identification
    if not check_credentials(username, password):
        stdscr.addstr(6, 0, "Nom d'utilisateur ou mot de passe incorrect.")
        stdscr.refresh()
        stdscr.getch()
        return  # Quitter si les informations d'identification sont incorrectes

    # Définir la structure du menu principal
    main_menu = {
        "title": "Main Menu",
        "options": [
            {
                "label": "User",
                "submenu": {
                    "title": "User Menu",
                    "options": [
                        {
                            "label": "Help",
                            "action": show_help
                        },
                        {
                            "label": "Crack",
                            "action": usr_crack_function
                        },
                        {
                            "label": "Files",
                            "action": show_files
                        },
                        {
                            "label": "Back"
                        }
                    ]
                }
            },
            {
                "label": "Root",
                "submenu": {
                    "title": "Root Menu",
                    "options": [
                        {
                            "label": "Option 2.1"
                        },
                        {
                            "label": "Option 2.2"
                        },
                        {
                            "label": "Commands",
                            "action": list_and_execute_commands
                        },
                        {
                            "label": "Back"
                        }
                    ]
                }
            },
            {
                "label": "Settings",
                "submenu": {
                    "title": "Settings Menu",
                    "options": [
                        {
                            "label": "Change Login"
                        },
                        {
                            "label": "Change Password"
                        },
                        {
                            "label": "Back"
                        }
                    ]
                }
            },
            {
                "label": "Quit",
                "action": lambda _: exit(0)
            }
        ]
    }

    show_menu(stdscr, main_menu)

if __name__ == '__main__':
    curses.wrapper(main)

