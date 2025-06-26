# gpt_style.py

import openai

openai.api_key = "TA_CLE_OPENAI"  # Remplace par ta clé

# Mapping des styles littéraires
AUTEURS = {
    "hugo": "Écris dans le style lyrique et grandiose de Victor Hugo.",
    "moliere": "Écris avec le ton théâtral et comique de Molière.",
    "baudelaire": "Utilise un style poétique, sombre et symboliste comme Baudelaire.",
    "camus": "Adopte un ton philosophique, simple et absurde comme Albert Camus.",
    "dumas": "Rends le style romanesque, héroïque et vivant comme Alexandre Dumas."
}

def gpt_reformuler(texte: str, style: str = "hugo") -> str:
    style_instruction = AUTEURS.get(style.lower(), AUTEURS["hugo"])

    messages = [
        {"role": "system", "content": f"Tu es un écrivain célèbre. {style_instruction}"},
        {"role": "user", "content": f"Reformule ce texte dans ton style : '{texte}'"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.9,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
