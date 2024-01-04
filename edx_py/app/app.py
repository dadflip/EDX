# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_makefile', methods=['POST'])
def generate_makefile():
    # Récupérer les données du formulaire HTML
    source_dir = request.form.get('source_dir')
    source_ext = request.form.get('source_ext')
    tool_type = request.form.get('tool_type')
    compiler = request.form.get('compiler')
    lib_flags = request.form.get('lib_flags')
    package_manager = request.form.get('package_manager')

    # Faire une requête POST vers le serveur Node.js
    nodejs_server_url = 'http://localhost:3000/generate_makefile'
    payload = {
        'source_dir': source_dir,
        'source_ext': source_ext,
        'tool_type': tool_type,
        'compiler': compiler,
        'lib_flags': lib_flags,
        'package_manager': package_manager,
    }

    response = requests.post(nodejs_server_url, data=payload)

    # Afficher le message de réussite ou d'erreur dans le navigateur
    return response.text

if __name__ == '__main__':
    app.run(debug=True)

