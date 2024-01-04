#!/bin/bash

# Check if whiptail is installed
if ! command -v whiptail &> /dev/null; then
    echo "whiptail is not installed."
    read -p "Do you want to install whiptail? (y/n): " install_choice

    if [ "$install_choice" == "y" ]; then
        sudo apt-get update
        sudo apt-get install whiptail
    else
        echo "Please install whiptail to use the text-based interface."
        exit 1
    fi
fi



# Menu to choose between compiler and package manager
TOOL_TYPE=$(whiptail --menu "Select Tool Type:" 15 60 2 \
    "1" "Compiler" \
    "2" "Package Manager" 3>&1 1>&2 2>&3)
tool_exit_status=$?
if [ $tool_exit_status -ne 0 ]; then
    echo "Tool type selection canceled."
    exit 1
fi

# Depending on the selected tool type, show the appropriate menu
if [ "$TOOL_TYPE" = "1" ]; then

	# Use whiptail to get user input
	SOURCE_DIR=$(whiptail --inputbox "Enter the source folder:" 10 60 --title "Source Folder" 3>&1 1>&2 2>&3)
	exit_status=$?
	if [ $exit_status -ne 0 ]; then
	    echo "Source folder entry canceled."
	    exit 1
	fi

	# Move to the selected source folder
	#cd "$SOURCE_DIR" || exit

	SOURCE_EXT=$(whiptail --checklist --title "Source Extensions" --separate-output \
	    "Select one or more source file extensions:" 20 60 15 \
	    "c" "C Source File" OFF \
	    "cpp" "C++ Source File" OFF \
	    "java" "Java Source File" OFF \
	    "py" "Python Source File" OFF \
	    "sh" "Shell Script" OFF \
	    "js" "JavaScript Source File" OFF \
	    "swift" "Swift Source File" OFF \
	    "rs" "Rust Source File" OFF \
	    "go" "Go Source File" OFF \
	    "hs" "Haskell Source File" OFF \
	    "ml" "OCaml Source File" OFF \
	    "f90" "Fortran 90 Source File" OFF \
	    "pas" "Pascal Source File" OFF \
	    "rb" "Ruby Source File" OFF \
	    "pl" "Perl Source File" OFF \
	    "scala" "Scala Source File" OFF \
	    "kt" "Kotlin Source File" OFF \
	    "lua" "Lua Source File" OFF \
	    "csharp" "C# Source File" OFF \
	    "php" "PHP Source File" OFF \
	    "html" "HTML File" OFF \
	    "css" "CSS File" OFF \
	    "sql" "SQL File" OFF \
	    "ts" "TypeScript Source File" OFF \
	    "dart" "Dart Source File" OFF \
	    "jsx" "React JSX File" OFF \
	    "tsx" "React TypeScript JSX File" OFF \
	    "yaml" "YAML File" OFF \
	    "json" "JSON File" OFF \
	    "xml" "XML File" OFF \
	    "markdown" "Markdown File" OFF \
	    3>&1 1>&2 2>&3)
	exit_status=$?
	if [ $exit_status -ne 0 ]; then
	    echo "Source extensions selection canceled."
	    exit 1
	fi

	# Compiler menu as radiolist
	COMPILER=$(whiptail --radiolist --title "Select Compiler" --separate-output \
	"Select the compiler to use:" 20 60 10 \
	"gcc" "GNU Compiler Collection" OFF \
	"g++" "GNU C++ Compiler" OFF \
	"clang" "Clang Compiler" OFF \
	"clang++" "Clang C++ Compiler" OFF \
	"javac" "Java Compiler" OFF \
	"python" "Python Interpreter" OFF \
	"bash" "Bash Interpreter" OFF \
	"cc" "C Compiler" OFF \
	"c++" "C++ Compiler" OFF \
	"nvcc" "NVIDIA CUDA Compiler" OFF \
	"fortran" "Fortran Compiler" OFF \
	"go" "Go Compiler" OFF \
	"rustc" "Rust Compiler" OFF \
	"swiftc" "Swift Compiler" OFF \
	"ghc" "Glasgow Haskell Compiler" OFF \
	"ocamlopt" "OCaml Compiler" OFF \
	"fpc" "Free Pascal Compiler" OFF \
	3>&1 1>&2 2>&3)
	comp_exit_status=$?
	if [ $comp_exit_status -ne 0 ]; then
	echo "Compiler selection canceled."
	exit 1
	fi

	# List of library flags in alphabetical order
	LIB_FLAGS=$(whiptail --checklist --title "Select Libraries" --separate-output \
	    "Select the libraries to link with:" 20 60 10 \
	    "dl" "dl Dynamic linking library" OFF \
	    "m" "m Math library" OFF \
	    "pthread" "pthread POSIX threads library" OFF \
	    "curses" "Curses library" OFF \
	    "readline" "Readline library" OFF \
	    "ssl" "SSL library" OFF \
	    "z" "zlib compression library" OFF \
	    "ncurses" "NCurses library" OFF \
	    "rt" "Real-time library" OFF \
	    "stdc++" "C++ Standard Library" OFF \
	    "sqlite3" "SQLite library" OFF \
	    "crypto" "OpenSSL Crypto library" OFF \
	    "udev" "udev library" OFF \
	    "curl" "cURL library" OFF \
	    "xml2" "Libxml2 library" OFF \
	    "boost" "Boost C++ library" OFF \
	    "iconv" "Iconv library" OFF \
	    "expat" "Expat library" OFF \
	    "jpeg" "JPEG library" OFF \
	    "png" "PNG library" OFF \
	    "tiff" "TIFF library" OFF \
	    "gif" "GIF library" OFF \
	    "pcre" "PCRE library" OFF \
	    "expat" "Expat library" OFF \
	    "iconv" "Iconv library" OFF \
	    "bz2" "Bzip2 library" OFF \
	    "lzma" "XZ Utils library" OFF \
	    "pq" "PostgreSQL library" OFF \
	    "X11" "X11 library" OFF \
	    "Xext" "X11 extensions library" OFF \
	    "Xt" "X Toolkit library" OFF \
	    "Xau" "X Authorization library" OFF \
	    "Xdmcp" "X Display Manager Control Protocol library" OFF \
	    "Xpm" "X Pixmap library" OFF \
	    "Xmu" "X Miscellaneous Utilities library" OFF \
	    "Xtst" "X Test library" OFF \
	    "Xrender" "X Rendering Extension library" OFF \
	    "Xfixes" "X Fixes library" OFF \
	    "Xi" "X Input extension library" OFF \
	    "Xinerama" "Xinerama library" OFF \
	    "Xrandr" "X Resize and Rotate library" OFF \
	    "Xcursor" "X Cursor library" OFF \
	    "Xcomposite" "X Composite extension library" OFF \
	    "Xdamage" "X Damage extension library" OFF \
	    "Xv" "X Video extension library" OFF \
	    "Xext" "X Extensions library" OFF \
	    "Xss" "X Screensaver extension library" OFF \
	    "Xxf86vm" "XFree86 Vidmode Extension library" OFF \
	    "your_library" "Custom library (specify below)" OFF \
	    3>&1 1>&2 2>&3)
	lib_exit_status=$?
	if [ $lib_exit_status -ne 0 ]; then
	    echo "Libraries selection canceled."
	    exit 1
	fi


	# Add custom library to LIB_FLAGS without newline characters
	if [[ "$LIB_FLAGS" == *"your_library"* ]]; then
	    CUSTOM_LIB=$(whiptail --inputbox "Enter the name of the custom library:" 10 60 --title "Custom Library" 3>&1 1>&2 2>&3)
	    exit_status=$?
	    if [ $exit_status -ne 0 ]; then
		echo "Custom library entry canceled."
		exit 1
	    fi

	    # Remove "your_library" from LIB_FLAGS
	    LIB_FLAGS=$(echo "$LIB_FLAGS" | sed 's/your_library//')

	    # Add custom library to LIB_FLAGS without newline characters
	    LIB_FLAGS="$LIB_FLAGS$CUSTOM_LIB"

	    # Remove newline characters from LIB_FLAGS
	    #LIB_FLAGS=$(echo "$LIB_FLAGS" | tr -d '\n')
	fi
	



echo $LIB_FLAGS


# Replace newlines with " - " and add " - " at the beginning if LIB_FLAGS is not empty
if [ -n "$LIB_FLAGS" ]; then
    LIB_FLAGS=$(echo "$LIB_FLAGS" | sed ':a;N;$!ba;s/\n/ -/g')
    LIB_FLAGS=$(echo "$LIB_FLAGS" | sed 's/^/ -/')
fi




# Generate Makefile in the selected source folder
cat <<EOF > Makefile
# Makefile generated by compile.sh

SRC_DIR := $SOURCE_DIR
SRC_EXT := $SOURCE_EXT
COMPILER := $COMPILER
LIB_FLAGS := $LIB_FLAGS

SRC_FILES := \$(foreach ext,\$(SRC_EXT),\$(wildcard \$(SRC_DIR)/*.\$(ext)))
OBJ_FILES := \$(patsubst \$(SRC_DIR)/%.c, \$(SRC_DIR)/%.o, \$(filter %.c, \$(SRC_FILES)))
OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.cpp, \$(SRC_DIR)/%.o, \$(filter %.cpp, \$(SRC_FILES)))
OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.java, \$(SRC_DIR)/%.class, \$(filter %.java, \$(SRC_FILES)))
OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.py, \$(SRC_DIR)/%, \$(filter %.py, \$(SRC_FILES)))
OBJ_FILES += \$(patsubst \$(SRC_DIR)/%.sh, \$(SRC_DIR)/%, \$(filter %.sh, \$(SRC_FILES)))

.PHONY: all clean

all: \$(OBJ_FILES)
	@echo "Compilation complete."

clean:
	@rm -f \$(OBJ_FILES)

\$(SRC_DIR)/%.o: \$(SRC_DIR)/%.c
	@echo "Compiling \$< with gcc..."
	@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

\$(SRC_DIR)/%.o: \$(SRC_DIR)/%.cpp
	@echo "Compiling \$< with g++..."
	@\$(COMPILER) -o \$@ -c \$< \$(LIB_FLAGS)

\$(SRC_DIR)/%.class: \$(SRC_DIR)/%.java
	@echo "Compiling \$< with javac..."
	@javac \$<

\$(SRC_DIR)/%: \$(SRC_DIR)/%.py
	@echo "Running \$< with python..."
	@python \$<

\$(SRC_DIR)/%: \$(SRC_DIR)/%.sh
	@echo "Running \$< with bash..."
	@bash \$<
EOF

	echo "Makefile generated successfully."
	cat Makefile

	exit 0
    
elif [ "$TOOL_TYPE" = "2" ]; then
    # Package Manager menu as checklist
    PACKAGE_MANAGER=$(whiptail --checklist --title "Select Package Manager" --separate-output \
        "Select the package manager to use:" 20 60 10 \
        "cargo" "Cargo (Rust Package Manager)" OFF \
        "npm" "npm (Node Package Manager)" OFF \
        "yarn" "Yarn (JavaScript Package Manager)" OFF \
        "maven" "Apache Maven" OFF \
        "gradle" "Gradle" OFF \
        "dotnet" ".NET Core SDK" OFF \
        "swift" "Swift Package Manager" OFF \
        "dart" "Dart SDK" OFF \
        "elixir" "Elixir Compiler" OFF \
        "julia" "Julia Compiler" OFF \
        "racket" "Racket Compiler" OFF \
        3>&1 1>&2 2>&3)
    pkg_exit_status=$?
    if [ $pkg_exit_status -ne 0 ]; then
        echo "Package manager selection canceled."
        exit 1
    fi
else
    echo "Invalid selection."
    exit 1
fi

# Print the selected tool(s)
echo "Selected Compiler: $COMPILER"
echo "Selected Package Manager: $PACKAGE_MANAGER"


