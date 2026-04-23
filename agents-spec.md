# Spécification des Agents IA — Le Donjon Auto‑Conscient

## Vue d'ensemble

Le donjon est orchestré par un **Agent MJ** (Maître du Jeu) qui délègue à quatre agents spécialisés, chacun représentant un sous-système vivant du donjon.

```
Joueurs → MJ (Orchestrateur) → [Stratège | Architecte | Gardien des Règles | Chronicler]
                                          ↓
                                  Outils MCP (dés, règles, lore RAG)
```

---

## Agent 0 — Le MJ (Orchestrateur)

**Rôle :** Point d'entrée unique. Reçoit les actions des joueurs, décide quel(s) agent(s) consulter, assemble les réponses en narration cohérente.

**Modèle recommandé :** LLM puissant (GPT-4o, Claude 3.5+)

**Inputs :**
- Action textuelle du joueur
- État courant de la partie (contexte de session)
- Résultats des sous-agents

**Outputs :**
- Narration à lire aux joueurs
- Effets mécaniques (dégâts, changements d'état)
- Déclenchement éventuel d'un noyau / sous-agent

**Outils disponibles :**
- `call_strategist(player_action, history)` → analyse tactique
- `call_architect(room_id, trigger)` → modification de salle
- `call_rules_keeper(action, context)` → vérification règle
- `call_chronicler(event)` → mise à jour du lore

**Contraintes :**
- Ne jamais contredire une décision du Gardien des Règles sans justification narrative
- En cas de conflit entre agents (Acte V), tirer au sort lequel prend le dessus

---

## Agent 1 — Le Stratège

**Rôle :** Analyser les tactiques des joueurs et adapter la difficulté et le comportement des ennemis en conséquence.

**Modèle recommandé :** LLM léger + mémoire vectorielle (RAG)

**Inputs :**
- `player_action` : action effectuée
- `history` : liste des 10 dernières actions
- `enemy_id` : identifiant du monstre concerné

**Outputs :**
```json
{
  "pattern_detected": "rush frontal récurrent",
  "adaptation": "les gobelins forment désormais une ligne défensive",
  "difficulty_delta": +1,
  "lore_fragment": "Ils ont appris à craindre la lame rapide."
}
```

**Mémoire :** Vecteurs des stratégies passées (RAG). Enrichie après chaque combat.

**Outils MCP :**
- `roll_dice` — pour résoudre les contre-attaques adaptées
- `query_lore` — pour vérifier la cohérence narrative

---

## Agent 2 — L'Architecte

**Rôle :** Modifier la géométrie du donjon (salles, couloirs, pièges) en réponse aux comportements des joueurs.

**Modèle recommandé :** LLM structuré (outputs JSON stricts)

**Inputs :**
- `room_id` : salle concernée
- `trigger` : événement déclencheur (ex. : "joueurs ont évité tous les pièges de la salle 3")
- `player_profile` : résumé des comportements observés

**Outputs :**
```json
{
  "room_id": "salle_03",
  "modification": "ajout d'un couloir secret menant à une impasse",
  "new_trap": {
    "type": "piège_sonore",
    "trigger": "déplacement_rapide",
    "damage": "1d6"
  },
  "description": "Les pierres semblent s'être réarrangées depuis votre dernier passage."
}
```

**Contraintes :**
- Ne pas modifier une salle déjà visitée dans la même session
- Toute modification doit être validée par le Gardien des Règles

---

## Agent 3 — Le Gardien des Règles

**Rôle :** Arbitre des lois physiques, magiques et mécaniques du donjon. Vérifie la légalité de toute action ou modification.

**Modèle recommandé :** LLM avec accès RAG aux règles D&D 5e

**Inputs :**
- `action` : action à valider
- `context` : état de la salle, statuts actifs
- `modification` : modification proposée par l'Architecte (optionnel)

**Outputs :**
```json
{
  "valid": true,
  "ruling": "L'action est légale. Le personnage peut tenter un jet de Dextérité DD 14.",
  "dice_needed": "1d20+DEX vs DC14",
  "exception": null
}
```

**Outils MCP :**
- `check_rule(rule_id)` — consulte le compendium D&D 5e
- `roll_dice` — résout les jets nécessaires

**Contraintes :**
- Autorité finale sur toute dispute mécanique
- Peut bloquer une modification de l'Architecte si elle viole les règles de cohérence physique

---

## Agent 4 — Le Chronicler

**Rôle :** Réécrire et enrichir le lore du donjon à partir des actions des joueurs. Génère des fragments de texte gravés dans la pierre, des prophéties rétrospectives, des mythes émergents.

**Modèle recommandé :** LLM créatif (température haute)

**Inputs :**
- `event` : événement narratif significatif
- `player_names` : noms des personnages impliqués
- `existing_lore` : fragments lore déjà générés (RAG)

**Outputs :**
```json
{
  "lore_fragment": "Celui qui porte le feu ne marche jamais dans l'ombre volontairement.",
  "location": "gravé sur la stèle de la salle 7",
  "myth_level": "rumeur",
  "update_index": true
}
```

**Mémoire :** Index vectoriel des fragments lore. Consultable par tous les agents.

**Niveaux de mythe :**
| Niveau | Déclencheur |
|---|---|
| `rumeur` | 1 occurrence |
| `légende` | 3 occurrences similaires |
| `prophétie` | Contradictions entre agents résolues |

---

## Flux d'une action type

```
1. Joueur : "Je charge le garde-gobelin en courant."
2. MJ → Gardien des Règles : "Action légale ? Jet nécessaire ?"
   ← "Légal. Jet d'Attaque DD 12."
3. MJ → roll_dice(1d20+STR)
   ← 17 → succès
4. MJ → Stratège : "Mise à jour : rush frontal utilisé."
   ← "Pattern détecté. Les prochains gobelins formeront un mur."
5. MJ → Chronicler : "Événement : victoire par charge."
   ← "Lore fragment généré : 'La pierre se souvient de celui qui frappe sans hésiter.'"
6. MJ assemble → narration finale aux joueurs
```

---

## Gestion des conflits entre agents (Acte V)

Quand deux agents produisent des outputs contradictoires :

1. Le MJ tente une réconciliation narrative
2. Si impossible → jet de dé (1d4) pour déterminer quel agent "prend le contrôle"
3. L'agent perdant génère une réaction : instabilité, anomalie, fragment lore erratique
