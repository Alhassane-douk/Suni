const auteursHorsLigne = {
  "Victor Hugo": (phrase) =>
    `« ${phrase.charAt(0).toUpperCase() + phrase.slice(1)}, soupira l'âme, telle une mer tourmentée sous les cieux en colère. »`,
  "Charles Baudelaire": (phrase) =>
    `Ô douleur ! ${phrase}. Ainsi parle le spleen dans la ville aux vapeurs d'opium.`,
  "Molière": (phrase) =>
    `Ma foi, ${phrase}, dit-il, en roulant les yeux comme un homme surpris par l'existence même de la vérité.`,
};

async function reformuler() {
  const phrase = document.getElementById("inputPhrase").value.trim();
  const auteur = document.getElementById("auteur").value;
  const resultatDiv = document.getElementById("resultat");

  if (!phrase) {
    resultatDiv.innerText = "Veuillez entrer une phrase.";
    return;
  }

  const horsLigne = Object.keys(auteursHorsLigne).includes(auteur);

  if (horsLigne) {
    const style = auteursHorsLigne[auteur];
    const result = style(phrase);
    resultatDiv.innerHTML = `<strong>${auteur}</strong> :<br>${result}`;
  } else {
    if (!navigator.onLine) {
      resultatDiv.innerHTML = `<span class="offline">Connexion requise pour ${auteur}. Veuillez vous connecter à Internet.</span>`;
      return;
    }

    resultatDiv.innerText = "Connexion à l’auteur en cours... 🧠";

    try {
      const response = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer TA_CLE_API" // Remplace par ta vraie clé
        },
        body: JSON.stringify({
          model: "gpt-4",
          messages: [
            {
              role: "system",
              content: `Tu es ${auteur}, célèbre écrivain. Réécris cette phrase avec ton style, ton vocabulaire, ton émotion : ${phrase}`
            },
            {
              role: "user",
              content: phrase
            }
          ],
          temperature: 0.9
        })
      });

      const data = await response.json();
      const texteReformule = data.choices[0].message.content;
      resultatDiv.innerHTML = `<strong>${auteur}</strong> :<br>${texteReformule}`;
    } catch (error) {
      console.error(error);
      resultatDiv.innerText = "Erreur lors de la communication avec l’API.";
    }
  }
}
