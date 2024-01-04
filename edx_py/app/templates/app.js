const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const morgan = require('morgan');

const app = express();
const port = 3000;

// Déclarez source_dir au niveau global du fichier
let source_dir;

// Utilise morgan pour enregistrer les logs dans un fichier
const logsStream = fs.createWriteStream(path.join(__dirname, 'logs.txt'), { flags: 'a' });
app.use(morgan('combined', { stream: logsStream }));

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/generate_makefile', (req, res) => {
    // Utilisez req.body.source_dir pour obtenir la valeur de source_dir
    source_dir = req.body.source_dir;
    const { source_ext, tool_type, compiler, lib_flags, package_manager } = req.body;

    // Ajoutez un log pour afficher la valeur de source_dir
    console.log('Source Directory:', source_dir);

    // Vérifiez si source_dir est défini
    if (!source_dir) {
        return res.status(400).json({ error: 'Le paramètre source_dir est manquant dans la requête.' });
    }

    // Générez le contenu du Makefile en fonction de l'entrée de l'utilisateur
    const makefileContent = `
    # Makefile généré par compile.sh

    SRC_DIR := ${source_dir}
    SRC_EXT := ${source_ext}
    COMPILER := ${compiler}
    LIB_FLAGS := ${lib_flags}

    SRC_FILES := \$(foreach ext,\$(SRC_EXT),\$(wildcard \$(SRC_DIR)/*.\$(ext)))
    OBJ_FILES := \$(patsubst \$(SRC_DIR)/%.c, \$(SRC_DIR)/%.o, \$(filter %.c, \$(SRC_FILES)))
    OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.cpp, \$(SRC_DIR)/%.o, \$(filter %.cpp, \$(SRC_FILES)))
    OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.java, \$(SRC_DIR)/%.class, \$(filter %.java, \$(SRC_FILES)))
    OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.py, \$(SRC_DIR)/%, \$(filter %.py, \$(SRC_FILES)))
    OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.sh, \$(SRC_DIR)/%, \$(filter %.sh, \$(SRC_FILES)))

    .PHONY: all clean

    all: \$(OBJ_FILES)
    \t@echo "Compilation complète."

    clean:
    \t@rm -f \$(OBJ_FILES)

    \$(SRC_DIR)/%.o: \$(SRC_DIR)/%.c
    \t@echo "Compilation de \$< avec gcc..."
    \t@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

    \$(SRC_DIR)/%.o: \$(SRC_DIR)/%.cpp
    \t@echo "Compilation de \$< avec g++..."
    \t@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

    \$(SRC_DIR)/%.class: \$(SRC_DIR)/%.java
    \t@echo "Compilation de \$< avec javac..."
    \t@javac \$<

    \$(SRC_DIR)/%: \$(SRC_DIR)/%.py
    \t@echo "Exécution de \$< avec python..."
    \t@python \$<

    \$(SRC_DIR)/%: \$(SRC_DIR)/%.sh
    \t@echo "Exécution de \$< avec bash..."
    \t@bash \$<`;

    // Enregistrez le contenu du Makefile dans un fichier
    const makefilePath = path.join(__dirname, 'public', source_dir, 'Makefile');
    fs.writeFileSync(makefilePath, makefileContent);

    // Créez le répertoire cible s'il n'existe pas
    const targetDir = path.join(__dirname, 'public', source_dir);
    fs.mkdirSync(targetDir, { recursive: true });

    // Importez tous les fichiers avec les extensions spécifiées
    if (source_ext) {
        fs.readdirSync(path.join(__dirname, 'public', source_dir)).forEach(file => {
            const fileExt = path.extname(file).substring(1);
            if (source_ext.includes(fileExt)) {
                const sourceFile = path.join(__dirname, 'public', source_dir, file);
                const targetFile = path.join(targetDir, file);
                fs.copyFileSync(sourceFile, targetFile);
            }
        });
    }

    // Déplacez le Makefile généré dans le répertoire cible
    const moveCommand = `mv ${makefilePath} ${targetDir}`;
    exec(moveCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`Erreur lors du déplacement du Makefile : ${error}`);
            // Envoyer une réponse avec l'erreur au navigateur
            return res.status(500).json({ error: `Erreur interne du serveur : ${error}` });
        }

        // Répondre avec succès et le chemin du Makefile généré
        const downloadPath = '/download_makefile';  // Le chemin correct pour télécharger le Makefile
        res.json({ success: 'Makefile généré avec succès.', downloadPath });
    });
});

// Route pour télécharger le Makefile
app.get('/download_makefile', (req, res) => {
    const makefilePath = path.join(__dirname, 'public', source_dir, 'Makefile');  // Correction du chemin du fichier Makefile

    // Affiche le chemin dans la console
    console.log('Chemin du Makefile:', makefilePath);

    // Assurez-vous que le fichier Makefile existe
    if (fs.existsSync(makefilePath)) {
        // Renvoie le fichier comme réponse avec le bon en-tête
        res.download(makefilePath, 'Makefile', (err) => {
            if (err) {
                console.error(`Erreur lors du téléchargement du Makefile : ${err}`);
                res.status(500).send('Erreur interne du serveur');
            }
        });
    } else {
        res.status(404).send('Makefile introuvable');
    }
});

// Ajoutez une route pour obtenir les logs depuis le navigateur
app.get('/logs', (req, res) => {
    res.sendFile(path.join(__dirname, 'logs.txt'));
});

app.listen(port, () => {
    console.log(`Serveur en écoute sur http://localhost:${port}`);
});

