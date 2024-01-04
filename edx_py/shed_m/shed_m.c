#include <ncurses.h>
#include <unistd.h>
#include <sched.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    // Initialisation de ncurses
    initscr();
    if (has_colors() == FALSE) {
        endwin();
        fprintf(stderr, "Le terminal ne supporte pas les couleurs.\n");
        return 1;
    }
    start_color();
    init_pair(1, COLOR_WHITE, COLOR_BLACK);
    init_pair(2, COLOR_GREEN, COLOR_BLACK);
    init_pair(3, COLOR_RED, COLOR_BLACK);

    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    // Obtention des valeurs limites pour le quantum de temps
    struct timespec quantum_limits;
    if (sched_rr_get_interval(0, &quantum_limits) != 0) {
        endwin();
        perror("Erreur lors de la récupération des valeurs du quantum de temps");
        return 1;
    }

    int min_priority = sched_get_priority_min(SCHED_RR);
    int max_priority = sched_get_priority_max(SCHED_RR);

    // Initialisation de la valeur du quantum de temps et de la priorité
    long int quantum = quantum_limits.tv_nsec;
    int priority = min_priority;

    // Affichage de l'interface graphique
    while (1) {
        clear();
        printw("Réglage du quantum de temps de l'ordonnanceur POSIX\n");
        printw("Utilisez les touches haut et bas pour ajuster la valeur (Esc pour quitter)\n");
        printw("Quantum actuel: %ld\n", quantum);

        // Obtention de la touche pressée
        int ch = getch();

        // Gestion des touches
        switch (ch) {
            case KEY_UP:
                if (quantum < quantum_limits.tv_nsec * 10) {
                    quantum += quantum_limits.tv_nsec;
                }
                break;
            case KEY_DOWN:
                if (quantum > quantum_limits.tv_nsec) {
                    quantum -= quantum_limits.tv_nsec;
                }
                break;
            case 27:  // 27 corresponds à la touche Escape (Esc)
                endwin(); // Fermeture de ncurses
                return 0;
            default:
                break;
        }

        // Appliquer la nouvelle valeur du quantum de temps
        struct sched_param param;
        param.sched_priority = priority;

        if (sched_setscheduler(0, SCHED_RR, &param) == -1) {
            attron(COLOR_PAIR(3));
            printw("Erreur lors du réglage de la politique d'ordonnancement\n");
            attroff(COLOR_PAIR(3));
            refresh();
            usleep(2000000);  // Attendre 2 secondes avant de quitter en cas d'erreur
            endwin();
            return 1;
        }

        struct timespec new_quantum;
        if (sched_rr_get_interval(0, &new_quantum) == 0) {
            // Utilisez l'intervalle récupéré pour afficher des informations, si nécessaire
        }

        // Rafraîchir l'écran
        attron(COLOR_PAIR(2));
        printw("Réglage réussi.\n");
        attroff(COLOR_PAIR(2));
        refresh();
        usleep(500000);  // Attendre 0.5 seconde avant de rafraîchir
    }

    return 0;
}
