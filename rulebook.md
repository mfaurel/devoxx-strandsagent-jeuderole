# Règles du Jeu — Le Donjon Auto‑Conscient

> Basé sur D&D 5e simplifié. Adapté pour une session de workshop de 2-3h avec des joueurs novices.

---

## Principes Fondamentaux

1. **Le dé décide, le donjon s'adapte.** Les jets de dés sont résolus normalement — mais le donjon *apprend* des résultats.
2. **Pas de mort permanente en workshop.** Un personnage à 0 PV est *inconscient*, pas mort (sauf choix narratif collectif).
3. **L'exploration compte autant que le combat.** Parler, négocier, observer rapportent autant d'XP que vaincre.
4. **Le MJ peut déléguer à un agent.** Quand le MJ consulte un agent IA, il annonce lequel et pourquoi — transparence pédagogique.

---

## Création de Personnage

### Caractéristiques (6 stats)

| Stat | Description |
|---|---|
| **FOR** Force | Combat physique, enfoncer des portes |
| **DEX** Dextérité | Esquive, discrétion, pièges |
| **CON** Constitution | Points de vie, endurance |
| **INT** Intelligence | Magie, déduction, connaissance |
| **SAG** Sagesse | Perception, intuition, survie |
| **CHA** Charisme | Persuasion, intimidation, parler au donjon |

**Distribution rapide (workshop) :** Répartir 72 points entre les 6 stats (min 8, max 18).

**Modificateur :** `(stat - 10) / 2` arrondi à l'inférieur.

### Points de Vie
`PV max = 10 + modificateur CON`

### Compétences choisies
Choisir 3 compétences parmi : Athlétisme, Discrétion, Arcanes, Histoire, Perception, Persuasion, Investigation, Survie, Intimidation.

Bonus de compétence : +3 (simplifié pour workshop)

---

## Résolution d'Actions

### Le Jet de Dé
`1d20 + modificateur de stat (+ bonus de compétence si applicable) ≥ Difficulté (DD)`

**Niveaux de difficulté :**
| DD | Niveau |
|---|---|
| 8 | Facile |
| 12 | Moyen |
| 15 | Difficile |
| 18 | Très difficile |
| 22 | Héroïque |

**Note :** Le Gardien des Règles (agent IA) fixe le DD en fonction du contexte.

### Avantage / Désavantage
- **Avantage** : lancer 2d20, garder le plus haut
- **Désavantage** : lancer 2d20, garder le plus bas
- Conditions : accordées par le MJ ou le Gardien des Règles selon la situation

### Succès Critique (20 naturel)
Réussite automatique + effet spectaculaire narratif (décrit par le MJ + Chronicler).

### Échec Critique (1 naturel)
Échec automatique + conséquence inattendue (le Stratège en tire une leçon immédiate).

---

## Combat

### Initiative
Chaque participant lance `1d20 + modificateur DEX`. Ordre décroissant.

### Tour de combat
1. **Déplacement** : jusqu'à 9m (30 pieds)
2. **Action** : attaque, sort, aide, dash, se cacher…
3. **Action bonus** *(si applicable selon la classe)*

### Attaque
`1d20 + modificateur FOR ou DEX + bonus de compétence ≥ Classe d'Armure (CA) de la cible`

**CA de base :** 10 + modificateur DEX (sans armure)

### Dégâts
Dépendent de l'arme ou du sort. Exemples :
| Arme | Dégâts |
|---|---|
| Dague | 1d4 + DEX |
| Épée courte | 1d6 + FOR ou DEX |
| Épée longue | 1d8 + FOR |
| Bâton de mage | 1d6 + INT |
| Sort : Projectile magique | 1d4+1 (automatique, pas de jet) |

### Mort et Inconscience
À 0 PV → inconscient. Jet de sauvegarde de mort à chaque tour (1d20, ≥ 10 = succès).
- 3 succès → stabilisé
- 3 échecs → mort (optionnel en workshop)
- Un allié peut stabiliser avec un jet de Médecine DD 10

---

## Mécanique Spéciale — L'Adaptation du Donjon

### Mémoire Tactique
Après chaque combat, le Stratège enregistre les tactiques utilisées.
À partir de la **2e rencontre** avec le même type d'ennemi, celui-ci bénéficie d'un bonus contextuel :
- +2 en CA contre la tactique répétée
- Peut anticiper une action déjà vue (Désavantage pour le joueur)

### Pièges Adaptatifs
Un piège déclenché et évité ne disparaît pas — il *évolue*.
- 1ère activation : piège standard
- 2e activation dans la même salle : piège modifié (DD +3, nouveau type de dégât)
- 3e activation : le piège est devenu un puzzle narratif

### Parler au Donjon
Compétence spéciale : **Persuasion (CHA)** vs DD fixé par le Gardien des Règles.
- DD 15 : Le donjon répond (fragments lore)
- DD 20 : Le donjon accepte une négociation (modification d'une règle locale)
- DD 25 : Accès au Cœur (Acte IV)
- Échec critique : Le Chronicler note le joueur comme "hostile"

### Reprogrammer un Sous-Système
Action de l'Acte IV. Nécessite :
1. Accès physique au Noyau correspondant
2. Jet d'Arcanes ou d'Investigation DD 18
3. Validation par le Gardien des Règles
4. Conséquence globale imprévisible (tirée par le MJ, table ci-dessous)

**Table des effets de reprogrammation (1d6) :**
| d6 | Effet |
|---|---|
| 1 | L'Architecte inverse tous les couloirs connus |
| 2 | Le Stratège oublie tous les profils joueurs |
| 3 | Le Chronicler réécrit 3 fragments au hasard |
| 4 | Le Gardien des Règles applique une règle aléatoire pendant 1h |
| 5 | Deux sous-systèmes entrent en conflit (Acte V anticipé) |
| 6 | Le donjon accepte le joueur comme "allié temporaire" |

---

## Repos

### Repos Court (10 min)
Récupérer `nd6` PV (n = niveau du personnage, ajouté CON mod).
Usage : 2 fois par session.

### Repos Long (nuit complète)
Récupérer tous les PV et ressources.
Non disponible à l'intérieur du donjon — le donjon ne dort jamais.

---

## Expérience et Progression

*Simplifié pour workshop — pas de niveaux, uniquement des jalons narratifs.*

**Jalons :**
- Atteindre la Couche 2 → Bonus de compétence +1
- Parler au donjon pour la première fois → Avantage permanent sur Persuasion envers le donjon
- Survivre à un conflit entre agents → Résistance aux dégâts psychiques

---

## Ressources Magiques

| Classe | Ressource | Rechargement |
|---|---|---|
| Mage | Emplacements de sorts (3/session) | Repos long |
| Clerc/Druide | Points de piété (4/session) | Repos long |
| Roublard | Points d'astuce (3/session) | Repos court |
| Guerrier | Second souffle (2/session) | Repos court |
