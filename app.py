
from flask import Flask, request, jsonify
from transformers import pipeline
import logging

app = Flask(__name__)

# Configuration du logger pour le debug
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chargement du modèle de reformulation (tu peux changer par un modèle plus littéraire si besoin)
logger.info("Chargement du modèle de reformulation...")
reformulateur = pipeline(
    "text2text-generation",
    model="Vamsi/T5_Paraphrase_Paws",  # À personnaliser plus tard
    tokenizer="Vamsi/T5_Paraphrase_Paws"
)
logger.info("Modèle chargé avec succès.")

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Bienvenue dans l'API de reformulation littéraire ! Utilisez /reformuler en POST."
    })

@app.route("/reformuler", methods=["POST"])
def reformuler_texte():
    data = request.get_json()

    if not data or 'texte' not in data:
        return jsonify({"error": "Aucun texte fourni."}), 400

    texte_original = data['texte'].strip()

    if not texte_original:
        return jsonify({"error": "Le texte est vide."}), 400

    try:
        logger.info(f"Texte reçu : {texte_original}")
        prompt = f"paraphrase: {texte_original} </s>"
        resultat = reformulateur(
            prompt,
            max_length=120,
            num_beams=5,
            num_return_sequences=1,
            temperature=1.5,
            repetition_penalty=1.2
        )
        texte_reformule = resultat[0]['generated_text']

        logger.info(f"Texte reformulé : {texte_reformule}")

        return jsonify({
            "original": texte_original,7
            "reformule": texte_reformule
        })

    except Exception as e:
        logger.error(f"Erreur lors de la reformulation : {str(e)}")
        return jsonify({"error": "Une erreur est survenue lors de la reformulation."}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    POST http://localhost:5000/reformuler
Content-Type: application/json

{
  "texte": "Je suis très fatigué de cette vie quotidienne.",
  "style": "baudelaire"
}
