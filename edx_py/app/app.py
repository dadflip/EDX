# app.py
from flask import Flask, render_template, request, jsonify
import requests
import os
import logging
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('public/index.html')
    
    
@app.route('/download_makefile', methods=['GET'])
def download_makefile():
    # Assurez-vous que source_dir est présent dans les arguments de requête
    source_dir = request.args.get('source_dir')

    if source_dir is None:
        return jsonify(error='source_dir parameter is missing'), 400

    makefile_path = os.path.join(__dirname, source_dir, 'Makefile')

    # Afficher dans la console
    app.logger.info(f"source_dir: {source_dir}")
    app.logger.info(f"makefile_path: {makefile_path}")

    if os.path.exists(makefile_path):
        return send_from_directory(os.path.dirname(makefile_path), 'Makefile', as_attachment=True)
    else:
        return jsonify(error='Makefile not found'), 404

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

    # Respond with success and the path to the generated Makefile
    downloadPath = '/download_makefile'  # Le chemin correct pour télécharger le Makefile
    return jsonify({'success': True, 'downloadPath': downloadPath})

if __name__ == '__main__':
    app.run(debug=True)

