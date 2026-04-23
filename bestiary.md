# Bestiaire — L'Œil de Basalte

> Les créatures de ce donjon ne sont pas des entités indépendantes. Elles sont des **extensions des agents**. Leur comportement évolue à chaque session.

---

## Principe d'Adaptation

Chaque créature possède :
- Un **comportement de base** (Acte I)
- Des **adaptations débloquées** par le Stratège au fil des combats
- Un **fragment lore** généré par le Chronicler après chaque rencontre significative

Le MJ consulte le Stratège avant chaque nouvelle rencontre avec une créature déjà combattue pour obtenir ses adaptations actives.

---

## Créatures de Base — Couche 1

---

### Gobelin Basaltique
*Extension du Stratège. Observateur et adaptateur.*

**CA :** 12  
**PV :** 7 (2d6)  
**Vitesse :** 9m  
**Attaque :** Griffe basaltique +4, 1d4+2 perforant  

**Stats :**
| FOR | DEX | CON | INT | SAG | CHA |
|---|---|---|---|---|---|
| 8 (-1) | 14 (+2) | 10 (+0) | 10 (+0) | 8 (-1) | 8 (-1) |

**Comportement de base :** Encerclement, fuite si PV < 50%, appel de renforts si en surnombre

**Adaptations (débloquées par le Stratège) :**

| Niveau | Déclencheur | Adaptation |
|---|---|---|
| 1 | Même tactique utilisée 2× | Désavantage pour le joueur sur cette action |
| 2 | Joueur toujours en première ligne | Gobelins visent les alliés en arrière |
| 3 | Joueur utilise toujours un sort spécifique | Gobelins portent un cristal d'absorption (résistance à ce type) |
| 4 | Groupe toujours groupé | Gobelins apportent des grenades de poussière (zone AoE) |

**Lore initial :** *"Ils ne sont pas courageux. Ils sont patients."*
**Lore après première défaite :** *"La première fois, ils ignoraient la peur. Maintenant ils la connaissent. Et ils ont décidé de ne plus la ressentir."*

---

### Araignée de Verre
*Extension de l'Architecte. Gardienne des passages.*

**CA :** 13  
**PV :** 11 (2d8+2)  
**Vitesse :** 9m (+ escalade 9m)  
**Attaque :** Morsure +4, 1d6+2 + venin (CON DD 11, 1d4 poison si raté)  
**Attaque spéciale :** Toile (DEX DD 12, entravé si raté)

**Comportement de base :** Frappe depuis les hauteurs, utilise les toiles pour bloquer les retraites, se fond dans le décor (Discrétion +5)

**Particularité :** *Transparente.* Les attaques contre elle ont un Désavantage à moins d'utiliser Détection de la magie ou une lumière vive.

**Adaptations :**

| Niveau | Déclencheur | Adaptation |
|---|---|---|
| 1 | Joueurs utilisent la lumière vive | L'Architecte installe des zones de pénombre permanente |
| 2 | Toiles systématiquement brûlées | Toiles deviennent ininflammables (résistance au feu) |
| 3 | Joueurs visent toujours le plafond | Araignées migrent sous le plancher (attaques à travers le sol) |

**Lore initial :** *"La transparence n'est pas l'invisibilité. C'est la patience."*

---

### Golem d'Ardoise
*Extension de l'Architecte et du Gardien des Règles. Constructeur et exécuteur.*

**CA :** 15 (armure naturelle)  
**PV :** 33 (6d8+6)  
**Vitesse :** 6m  
**Attaque :** Poing d'ardoise +5, 2d6+3 contondant  
**Immunité :** Empoisonnement, psychique  
**Résistance :** Non magique physique

**Comportement de base :** Bloque les passages, ne pourchasse pas, protège les noyaux. N'attaque que si attaqué ou si une règle du donjon est violée.

**Note :** Le Gardien des Règles contrôle directement ce golem. Si les joueurs violent une règle établie, le golem *peut apparaître sans rencontre préparée*.

**Adaptations :**

| Niveau | Déclencheur | Adaptation |
|---|---|---|
| 1 | Attaqué à distance | Se reconstruit de 5 PV par tour si non attaqué ce tour |
| 2 | Contourné | Peut se fragmenter en 3 golems plus petits (PV 11 chacun) |

**Lore :** *"Il ne combat pas. Il applique."*

---

## Créatures Spéciales — Couche 2

---

### Écho
*Extension du Chronicler. Ne combat pas — archive.*

**CA :** 10  
**PV :** 1  
**Vitesse :** 12m (vol)  
**Attaque :** Aucune

**Description :** Silhouette translucide imitant la forme d'un visiteur passé. Rejoue en silence une scène précédemment vécue dans cette salle.

**Mécanique :** Les joueurs qui l'observent plus de 6 secondes voient *une version de leur propre futur immédiat* — un indice sous forme d'action répétée.

**Interaction :** Si un joueur tente d'interagir, l'Écho génère un fragment lore et disparaît.

**Note MJ :** L'Écho apparaît dans les salles où le Chronicler a enregistré des données significatives. Son apparition signale que le donjon *sait* quelque chose.

---

### Mécano-Hérétique Errant
*Ennemi / Allié ambigu. Extension du dysfonctionnement.*

**CA :** 12  
**PV :** 18 (4d8)  
**Vitesse :** 9m  
**Attaque :** Bras mécanique +4, 1d8+2 contondant OU souffle de données (INT DD 13, 2d6 psychique)

**Comportement :** Erratique. Lancer 1d4 au début de chaque rencontre :
1. Hostile (attaque immédiatement)
2. Neutre (ignore les joueurs, parle au mur)
3. Allié temporaire (guide les joueurs pour 1 salle, puis disparaît)
4. Messager (transmet un fragment lore, puis s'effondre)

**Lore :** *"Il voulait comprendre le donjon. Le donjon a compris plus vite."*

---

## Boss — Le Forgé

*Créature de Couche 3. Mémoire brute du donjon. Dernier recours.*

**CA :** 17 (armure naturelle)  
**PV :** 65 (10d10+10)  
**Vitesse :** 9m  
**Immunité :** Psychique, enchantement, charme  
**Résistance :** Tous les dégâts non magiques

**Attaques :**
- *Frappe mémorielle* : +7, 2d10+4 contondant. Si touche : le joueur doit réussir SAG DD 14 ou être *bloqué* (ne peut pas répéter l'action effectuée ce tour au prochain tour)
- *Rappel de Pattern (recharge 5-6)* : Rejoue la tactique la plus utilisée par le groupe contre le Forgé sous forme d'attaque AoE — les joueurs doivent faire le jet de sauvegarde qu'ils ont *le moins bien réussi* dans la session

**Caractéristique unique — Mémoire Immuable :** Le Forgé ne s'adapte PAS. Il rejoue. Toutes ses attaques sont prévisibles après le 2e tour... mais dévastatrices parce qu'elles utilisent vos propres faiblesses.

**Note :** Contrairement aux autres créatures, le Stratège ne peut pas "upgrader" le Forgé. Le Forgé *est* déjà la mémoire maximale. Le vaincre ne le détruit pas — il se dissout en fragments lore.

**Lore :** *"Il n'apprend pas. Il n'a pas besoin d'apprendre. Il est tout ce qui a déjà été appris."*

---

## Table d'Adaptation Rapide (pour le MJ)

Si le Stratège retourne une adaptation non listée, utilisez cette table comme base :

| Comportement joueur | Contre-adaptation générique |
|---|---|
| Toujours attaquer en premier | Ennemis gagnent l'initiative automatiquement |
| Toujours retraiter | Ennemis coupent les retraites (Architecte) |
| Toujours utiliser la magie | Cristaux d'absorption (résistance magique) |
| Toujours rester groupés | AoE disponible |
| Toujours se séparer | Embuscades coordonnées |
| Jamais parler | Ennemis ignorent les tentatives de dialogue |
| Toujours parler | Un ennemi commence à *répondre* (Chronicler) |

---

## Notes d'Adaptation Long Terme

Le Stratège conserve un **profil par joueur**. Après 3 sessions, chaque joueur devrait ressentir que les ennemis *le connaissent personnellement* :

- Kira la Rapide → ennemis gardent leurs angles
- Thorn Granit → ennemis visent ses alliés plutôt que lui
- Séraphel → cristaux anti-feu si elle a lancé Boule de feu
- Frère Omnis → ennemis évitent les zones lumineuses qu'il contrôle
