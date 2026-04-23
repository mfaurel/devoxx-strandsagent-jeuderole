# Guide du Maître du Jeu — Orchestration des Agents IA

> Ce guide est destiné au MJ humain. Il explique comment collaborer avec les agents IA sans perdre le contrôle de la table.

---

## Votre Rôle

Vous n'êtes plus omniscient. Vous êtes **chef d'orchestre**.

Votre travail :
- Recevoir les actions des joueurs
- Décider quel(s) agent(s) consulter
- Assembler les réponses en narration fluide
- Gérer les conflits quand les agents se contredisent
- Maintenir le rythme et l'immersion

Ce que vous **ne faites plus** seul : inventer les adaptations tactiques, modifier la géométrie des salles, générer le lore à la volée, arbitrer les règles complexes.

---

## Quand Consulter Quel Agent

| Situation | Agent à consulter |
|---|---|
| Les joueurs utilisent une tactique pour la 2e fois | Stratège |
| Les joueurs passent du temps dans une salle déjà visitée | Architecte |
| Règle ambiguë, action inhabituelle | Gardien des Règles |
| Événement narratif fort (mort, victoire inattendue, trahison) | Chronicler |
| Les joueurs tentent de parler au donjon | Tous (séquence spéciale) |
| Conflit entre deux agents | Voir section "Gestion des Conflits" |

**Règle du pouce :** Si vous hésitez, consultez d'abord le Gardien des Règles. Il valide, puis vous passez aux autres.

---

## Protocole d'une Action

```
1. Joueur annonce son action
2. MJ évalue : mécanique ? tactique ? narrative ? géographique ?
3. MJ consulte le(s) agent(s) concerné(s)
4. MJ reçoit les outputs
5. MJ vérifie la cohérence (contradictions ?)
6. MJ narre le résultat
7. MJ met à jour le contexte de session
```

**Exemple :**
> Joueur : "Je tente de désarmer le piège en utilisant mes outils de voleur."

1. Mécanique + potentiellement tactique (si c'est le 2e piège du même type)
2. Gardien des Règles → DD du jet, type de compétence
3. Stratège → "Ce piège a-t-il déjà été tenté ? Adaptation ?"
4. Résultat : jet DD 14 (Dextérité + Outils de voleur). Si c'est le 2e piège du même type, DD 17.
5. Narre le résultat + éventuel fragment Chronicler si succès/échec remarquable.

---

## Transparence Pédagogique

Dans le contexte Devoxx, **annoncez vos appels d'agents à voix haute** :

> "Je consulte le Stratège pour voir si le gobelin a appris quelque chose des combats précédents…"
> "Le Gardien des Règles me dit que ce jet est un DD 15 de Perception…"
> "Le Chronicler vient de générer ce fragment de lore — il apparaît gravé dans le mur devant vous."

Cela sert deux objectifs :
1. **Immersion** : le donjon "pense" visible
2. **Pédagogie** : les participants comprennent l'orchestration multi-agents en temps réel

---

## Gestion des Conflits entre Agents

### Niveau 1 — Contradiction mineure
*Exemple : le Stratège dit "les gobelins fuient" mais l'Architecte a bloqué le couloir de fuite.*

→ Réconciliation narrative simple : "Les gobelins tentent de fuir mais se retrouvent piégés par la géométrie changeante du donjon. Ils se retournent, paniqués."

### Niveau 2 — Contradiction majeure
*Exemple : le Gardien des Règles interdit une modification que l'Architecte vient de valider.*

→ Annoncez le conflit aux joueurs : "Quelque chose dans le donjon semble… hésiter. Les murs craquent. Un piège s'active à moitié puis s'arrête."

→ Tirez 1d4 : l'agent avec le plus bas chiffre "gagne". L'autre génère une anomalie.

### Niveau 3 — Acte V (Perte de Contrôle)
*Tous les agents en désaccord simultané.*

→ C'est le **moment pédagogique central**. Embrassez le chaos.
→ Tirez au sort quel agent prend le contrôle à chaque tour (1d4, 1=Stratège, 2=Architecte, 3=Gardien, 4=Chronicler).
→ Chaque agent applique sa logique sans tenir compte des autres.
→ Narrativement : le donjon *se fragmente*.

---

## Calibration de la Difficulté

### Trop facile ?
- Demandez au Stratège une adaptation immédiate
- Demandez à l'Architecte de modifier la salle suivante
- Ajoutez un fragment Chronicler qui signale que "le donjon a remarqué"

### Trop difficile ?
- Le donjon peut "tester" plutôt que "détruire" — ajustez les intentions des ennemis
- Le Gardien des Règles peut offrir une règle d'exception justifiée narrativement
- Un Mécano-Hérétique peut apparaître comme allié temporaire

### Joueurs bloqués ?
- Le Chronicler génère un fragment comme indice
- Une anomalie architecturale révèle un passage
- Le donjon "parle" involontairement — un sous-système génère du bruit que les joueurs peuvent interpréter

---

## La Séquence "Parler au Donjon"

Quand les joueurs tentent d'initier un dialogue avec le donjon :

**Étape 1 — Vérification**
Gardien des Règles : le joueur doit avoir visité au moins la Couche 2 et réussi un jet de CHA DD 15.

**Étape 2 — Réponse du Donjon**
Consultez TOUS les agents simultanément. Assemblez leurs outputs comme une voix chorale, parfois contradictoire :

> "Vous avez combattu [x] fois. Vos schémas sont [prévisibles / fascinants / inefficaces]. La salle [n] sera [différente / la même / absente] à votre prochain passage. [Votre nom dans le lore] signifie maintenant [fragment Chronicler]."

**Étape 3 — Négociation possible (DD 20+)**
Le joueur peut proposer une règle locale. Le Gardien des Règles valide. L'Architecte implémente. Le Stratège ajuste. Le Chronicler documente.

---

## Notes de Rythme pour Workshop

| Phase | Durée | Agents actifs |
|---|---|---|
| Introduction + création perso | 20 min | Aucun |
| Acte I — Premières salles | 30 min | Gardien des Règles, Stratège |
| Acte II — Découverte des noyaux | 20 min | Architecte, Chronicler |
| Acte III — Le donjon contre-attaque | 25 min | Tous |
| Acte IV — Dialogue | 20 min | Tous (séquence spéciale) |
| Acte V/VI — Résolution | 25 min | Conflits, décision finale |

**Total estimé : ~2h30**

Si le temps manque, compressez les Actes II et III. L'Acte IV (dialogue) et l'Acte V (conflit) sont les moments pédagogiques irremplaçables.

---

## Checklist Pré-Session

- [ ] Agents démarrés et testés (appel de test sur chaque agent)
- [ ] Index RAG du lore chargé (lore.md indexé)
- [ ] Règles D&D chargées dans le Gardien des Règles
- [ ] Mémoire tactique du Stratège vide (nouvelle session)
- [ ] Contexte de session initialisé (noms des joueurs, personnages)
- [ ] Dés physiques disponibles (backup si les outils MCP sont lents)
- [ ] `storyline.md` ouvert pour suivre les actes

---

## Ce Que les Agents Ne Font Pas

- **Ne prennent pas de décisions narratives finales** — c'est vous
- **Ne gèrent pas les émotions à table** — c'est vous
- **Ne s'adaptent pas au rythme de la table** — c'est vous
- **Ne savent pas quand un joueur est perdu** — c'est vous

Les agents sont des *outils puissants avec des angles morts*. Votre jugement humain reste la couche supérieure de l'orchestration.
