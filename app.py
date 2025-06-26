from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import json
import os

app = Flask(__name__)

# NLP pipeline
rephraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

# Charger les textes enregistrés
SAVE_FILE = "saved_texts.json"
if not os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reform', methods=['POST'])
def reform_text():
    data = request.get_json()
    input_text = data.get("text")

    if not input_text:
        return jsonify({"error": "Texte vide"}), 400

    reformulated = rephraser(f"paraphrase: {input_text}", max_length=200, do_sample=True, top_k=120, top_p=0.95, num_return_sequences=1)

    output = reformulated[0]['generated_text']

    # Enregistrer dans le fichier
    with open(SAVE_FILE, 'r+') as f:
        saved = json.load(f)
        saved.append({"original": input_text, "reformulated": output})
        f.seek(0)
        json.dump(saved, f, indent=4)

    return jsonify({"result": output})

@app.route('/saved')
def get_saved():
    with open(SAVE_FILE) as f:
        saved = json.load(f)
    return jsonify(saved)

if __name__ == '__main__':
    app.run(debug=True)
