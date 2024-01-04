#include <gtk/gtk.h>
#include <proc/readproc.h>

void on_row_activated(GtkTreeView *treeview, GtkTreePath *path, GtkTreeViewColumn *column, gpointer user_data) {
    GtkTreeModel *model;
    GtkTreeIter iter;

    model = gtk_tree_view_get_model(treeview);
    if (gtk_tree_model_get_iter(model, &iter, path)) {
        gchar *pid_str;
        gtk_tree_model_get(model, &iter, 0, &pid_str, -1);

        // Vous pouvez utiliser pid_str pour obtenir des informations supplémentaires sur le processus
        // par exemple en lisant le contenu de /proc/pid_str

        g_free(pid_str);
    }
}

void refresh_processes(GtkListStore *list_store) {
    PROCTAB *proc = openproc(PROC_FILLSTATUS | PROC_FILLCOM);
    proc_t proc_info;

    gtk_list_store_clear(list_store);

    while (readproc(proc, &proc_info) != NULL) {
        gchar *pid_str = g_strdup_printf("%d", proc_info.tid);
        gchar *cmdline = proc_info.cmdline ? proc_info.cmdline : "";

        GtkTreeIter iter;
        gtk_list_store_append(list_store, &iter);
        gtk_list_store_set(list_store, &iter, 0, pid_str, 1, cmdline, -1);

        g_free(pid_str);
    }

    closeproc(proc);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Explorateur de Processus");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 300);
    gtk_container_set_border_width(GTK_CONTAINER(window), 10);

    GtkListStore *list_store;
    GtkWidget *treeview;
    GtkTreeViewColumn *column;
    GtkCellRenderer *renderer;

    list_store = gtk_list_store_new(2, G_TYPE_STRING, G_TYPE_STRING);

    treeview = gtk_tree_view_new_with_model(GTK_TREE_MODEL(list_store));
    g_object_unref(list_store);

    renderer = gtk_cell_renderer_text_new();

    column = gtk_tree_view_column_new_with_attributes("PID", renderer, "text", 0, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column);

    renderer = gtk_cell_renderer_text_new();
    column = gtk_tree_view_column_new_with_attributes("Commande", renderer, "text", 1, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column);

    gtk_tree_view_set_headers_visible(GTK_TREE_VIEW(treeview), TRUE);

    gtk_tree_view_set_activate_on_single_click(GTK_TREE_VIEW(treeview), TRUE);
    g_signal_connect(treeview, "row-activated", G_CALLBACK(on_row_activated), NULL);

    GtkWidget *scrolled_window = gtk_scrolled_window_new(NULL, NULL);
    gtk_container_add(GTK_CONTAINER(scrolled_window), treeview);

    gtk_container_add(GTK_CONTAINER(window), scrolled_window);

    GtkWidget *button_refresh = gtk_button_new_with_label("Actualiser");
    g_signal_connect_swapped(button_refresh, "clicked", G_CALLBACK(refresh_processes), list_store);

    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 5);
    gtk_box_pack_start(GTK_BOX(box), button_refresh, FALSE, FALSE, 0);

    gtk_box_pack_start(GTK_BOX(box), scrolled_window, TRUE, TRUE, 0);
    gtk_container_add(GTK_CONTAINER(window), box);

    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_widget_show_all(window);

    refresh_processes(list_store);

    gtk_main();

    return 0;
}
