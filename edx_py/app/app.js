// app.js

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/generate_makefile', (req, res) => {
    const { source_dir, source_ext, tool_type, compiler, lib_flags, package_manager } = req.body;

    // Generate Makefile content based on user input
    const makefileContent = `
# Makefile generated by compile.sh

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
\t@echo "Compilation complete."

clean:
\t@rm -f \$(OBJ_FILES)

\$(SRC_DIR)/%.o: \$(SRC_DIR)/%.c
\t@echo "Compiling \$< with gcc..."
\t@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

\$(SRC_DIR)/%.o: \$(SRC_DIR)/%.cpp
\t@echo "Compiling \$< with g++..."
\t@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

\$(SRC_DIR)/%.class: \$(SRC_DIR)/%.java
\t@echo "Compiling \$< with javac..."
\t@javac \$<

\$(SRC_DIR)/%: \$(SRC_DIR)/%.py
\t@echo "Running \$< with python..."
\t@python \$<

\$(SRC_DIR)/%: \$(SRC_DIR)/%.sh
\t@echo "Running \$< with bash..."
\t@bash \$<`;

    // Save the Makefile content to a file
    const makefilePath = path.join(__dirname, 'public', 'Makefile');
    fs.writeFileSync(makefilePath, makefileContent);

    // Execute a command to move the generated Makefile to the user-specified destination
    const moveCommand = `mv ${makefilePath} ${path.join(source_dir, 'Makefile')}`;
    exec(moveCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error moving Makefile: ${error}`);
            return res.status(500).send('Internal Server Error');
        }

        // Respond with success and the path to the generated Makefile
        const successMessage = `Makefile generated successfully. Download it from: ${path.join(source_dir, 'Makefile')}`;
        res.status(200).send(successMessage);
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
