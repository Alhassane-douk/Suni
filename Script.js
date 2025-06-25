// Notes estimées d'Einstein
const einsteinNotes = {
  maths: 20,
  physique: 19,
  chimie: 15
};

document.getElementById("notes-form").addEventListener("submit", function(e) {
  e.preventDefault();

  const maths = parseFloat(e.target.maths.value);
  const physique = parseFloat(e.target.physique.value);
  const chimie = parseFloat(e.target.chimie.value);

  let totalPossible = 0;
  let totalUtilisateur = 0;

  if (!isNaN(maths)) {
    totalPossible += einsteinNotes.maths;
    totalUtilisateur += Math.min(maths, einsteinNotes.maths);
  }

  if (!isNaN(physique)) {
    totalPossible += einsteinNotes.physique;
    totalUtilisateur += Math.min(physique, einsteinNotes.physique);
  }

  if (!isNaN(chimie)) {
    totalPossible += einsteinNotes.chimie;
    totalUtilisateur += Math.min(chimie, einsteinNotes.chimie);
  }

  const pourcentage = Math.round((totalUtilisateur / totalPossible) * 100);

  const resultat = document.getElementById("resultat");
  resultat.innerText = `Tu atteins ${pourcentage}% des notes d'Einstein ! 🧠`;

  if (pourcentage >= 90) {
    resultat.innerText += "\nIncroyable ! Tu marches sur ses traces ! 🚀";
  } else if (pourcentage >= 60) {
    resultat.innerText += "\nBeau travail, continue comme ça ! 💪";
  } else {
    resultat.innerText += "\nNe lâche rien, chaque génie commence quelque part ! ✨";
  }
});
