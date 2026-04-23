# Serveurs MCP & Outils — Le Donjon Auto‑Conscient

> Spécification technique des outils MCP nécessaires pour alimenter les agents IA du donjon.

---

## Architecture Générale

```
┌─────────────────────────────────────────────────────────────┐
│                     Agent MJ (Orchestrateur)                │
└──────┬──────────┬────────────┬──────────────┬───────────────┘
       │          │            │              │
  Stratège   Architecte   Gardien      Chronicler
       │          │         Règles           │
       └──────────┴────────────┴─────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        dice-server    rules-server    lore-server
        (MCP)          (MCP + RAG)     (MCP + RAG)
```

---

## Serveur 1 — `dice-server`

**Responsabilité :** Lancer les dés. Simple, déterministe, auditable.

**Protocole :** MCP  
**Implémentation suggérée :** Node.js ou Python, stateless

### Outils exposés

#### `roll_dice`
Lance un ou plusieurs dés.

**Input :**
```json
{
  "expression": "2d6+3",
  "reason": "attaque du gobelin contre Kira"
}
```

**Output :**
```json
{
  "expression": "2d6+3",
  "rolls": [4, 2],
  "modifier": 3,
  "total": 9,
  "reason": "attaque du gobelin contre Kira",
  "timestamp": "2026-04-23T14:32:01Z"
}
```

**Formats supportés :** `NdX`, `NdX+M`, `NdX-M`, `NdX adv` (avantage), `NdX dis` (désavantage)

**Notes de sécurité :**
- RNG cryptographiquement sûr (`crypto.randomInt` ou `secrets.randbelow`)
- Logs de tous les jets pour auditabilité (rejouer une session)
- Pas d'état — chaque appel est indépendant

---

## Serveur 2 — `rules-server`

**Responsabilité :** Arbitrer les règles D&D 5e. Répondre aux questions mécaniques des agents.

**Protocole :** MCP  
**Implémentation suggérée :** Python + LlamaIndex ou LangChain avec RAG sur le SRD D&D 5e

### Source de données
- **SRD D&D 5e** (Systems Reference Document — licence OGL, open source)
- `rulebook.md` du projet (règles custom du donjon)
- Index vectoriel (ChromaDB, Qdrant, ou Weaviate)

### Outils exposés

#### `check_rule`
Vérifie une règle ou arbitre une situation mécanique.

**Input :**
```json
{
  "action": "Le joueur tente de désarmer un piège avec ses outils de voleur",
  "context": {
    "room_id": "salle_03",
    "trap_type": "mécanique",
    "player_stats": { "DEX": 18, "proficient_thieves_tools": true }
  }
}
```

**Output :**
```json
{
  "valid": true,
  "ruling": "Action légale. Jet de Dextérité (Outils de voleur) DD 14.",
  "dice_needed": "1d20+4 vs DC14",
  "source": "PHB p.154 + rulebook.md §Pièges adaptatifs",
  "exception": null,
  "custom_rule_applied": false
}
```

#### `get_dc`
Retourne la difficulté appropriée pour une action donnée.

**Input :**
```json
{
  "action_type": "perception",
  "context": "couloir sombre, piège camouflé",
  "adaptation_level": 2
}
```

**Output :**
```json
{
  "base_dc": 14,
  "adaptation_bonus": 3,
  "final_dc": 17,
  "justification": "Piège de 2e génération (adaptatif niveau 2)"
}
```

---

## Serveur 3 — `lore-server`

**Responsabilité :** Stocker, indexer et retrouver les fragments de lore générés par le Chronicler. Base de mémoire narrative du donjon.

**Protocole :** MCP  
**Implémentation suggérée :** Python + ChromaDB (local) ou Qdrant

### Source de données
- `lore.md` — lore initial (seed)
- Fragments générés dynamiquement au cours des sessions
- Index vectoriel mis à jour en temps réel

### Outils exposés

#### `query_lore`
Recherche sémantique dans le lore existant.

**Input :**
```json
{
  "query": "joueur utilisant le feu",
  "top_k": 3,
  "filters": {
    "myth_level": ["rumeur", "légende"]
  }
}
```

**Output :**
```json
{
  "results": [
    {
      "fragment": "Celui qui brûle toujours craint le silence.",
      "location": "salle_07",
      "myth_level": "légende",
      "score": 0.92
    }
  ]
}
```

#### `add_lore_fragment`
Ajoute un nouveau fragment généré par le Chronicler.

**Input :**
```json
{
  "fragment": "La lame rapide préfère les corridors étroits.",
  "context": {
    "player": "Kira la Rapide",
    "event": "victoire par flanc droit en couloir",
    "session": "session_01"
  },
  "location": "salle_05",
  "myth_level": "rumeur"
}
```

**Output :**
```json
{
  "id": "lore_042",
  "indexed": true,
  "duplicate_detected": false,
  "upgraded_to": null
}
```

#### `upgrade_myth_level`
Promu automatiquement quand un pattern atteint le seuil de récurrence.

**Seuils :**
| De | Vers | Déclencheur |
|---|---|---|
| `rumeur` | `légende` | Fragment similaire apparu 3× |
| `légende` | `prophétie` | Fragment validé par 2 agents différents |

---

## Serveur 4 — `memory-server` *(optionnel avancé)*

**Responsabilité :** Mémoire persistante cross-sessions pour le Stratège.

**Protocole :** MCP  
**Implémentation :** Python + SQLite ou PostgreSQL

### Outils exposés

#### `store_player_pattern`
```json
{
  "player_id": "kira",
  "pattern": "flanc_droit",
  "occurrences": 3,
  "session": "session_01"
}
```

#### `get_player_profile`
```json
{
  "player_id": "kira"
}
```
→ Retourne le profil tactique complet avec tous les patterns enregistrés.

---

## Configuration des Agents

### Variables d'environnement

```env
# dice-server
DICE_SERVER_PORT=3001
DICE_LOG_PATH=./logs/dice.jsonl

# rules-server
RULES_SERVER_PORT=3002
SRD_INDEX_PATH=./indexes/srd
CUSTOM_RULES_PATH=./rulebook.md

# lore-server
LORE_SERVER_PORT=3003
LORE_INDEX_PATH=./indexes/lore
LORE_SEED_PATH=./lore.md

# memory-server
MEMORY_SERVER_PORT=3004
MEMORY_DB_PATH=./data/memory.db

# LLM (partagé par tous les agents)
LLM_PROVIDER=openai          # ou anthropic, ollama, etc.
LLM_MODEL=gpt-4o
LLM_API_KEY=<votre_clé>
```

### Configuration MCP (exemple `mcp.json`)

```json
{
  "mcpServers": {
    "dice": {
      "command": "node",
      "args": ["./servers/dice-server/index.js"],
      "env": { "PORT": "3001" }
    },
    "rules": {
      "command": "python",
      "args": ["./servers/rules-server/main.py"],
      "env": { "PORT": "3002" }
    },
    "lore": {
      "command": "python",
      "args": ["./servers/lore-server/main.py"],
      "env": { "PORT": "3003" }
    }
  }
}
```

---

## Flux A2A (Agent to Agent)

Les agents communiquent via le protocole **A2A** pour les cas de coordination :

```
Stratège → Chronicler : "Enregistre ce pattern tactique comme fragment lore"
Architecte → Gardien des Règles : "Cette modification est-elle légale ?"
Chronicler → Lore-server : "Indexe ce nouveau fragment"
MJ → Tous : "Broadcast : Acte V déclenché — conflit de gouvernance"
```

**Format de message A2A :**
```json
{
  "from": "stratege",
  "to": "chronicler",
  "type": "lore_request",
  "payload": {
    "event": "pattern_detected",
    "data": "rush_frontal × 3",
    "suggested_fragment": "La vitesse sans direction finit par être prévisible."
  },
  "session_id": "session_01",
  "timestamp": "2026-04-23T15:01:22Z"
}
```

---

## Stack Technique Recommandée

| Composant | Option simple | Option avancée |
|---|---|---|
| LLM | OpenAI GPT-4o | Anthropic Claude / Ollama local |
| Framework agent | LangChain | LlamaIndex Agents / CrewAI |
| Protocole orchestration | MCP SDK (Python/JS) | MCP + A2A custom |
| Mémoire vectorielle | ChromaDB (local) | Qdrant / Weaviate |
| Persistance | SQLite | PostgreSQL |
| Logs | JSONL fichier local | OpenTelemetry |

---

## Checklist de Démarrage

```bash
# 1. Indexer le lore initial
python servers/lore-server/index_seed.py --input lore.md

# 2. Indexer les règles SRD
python servers/rules-server/index_srd.py --input data/srd5e.md

# 3. Démarrer les serveurs MCP
node servers/dice-server/index.js &
python servers/rules-server/main.py &
python servers/lore-server/main.py &

# 4. Tester les outils
python tools/test_dice.py
python tools/test_rules.py "Peut-on désarmer un piège sans outils ?"
python tools/test_lore.py "feu"

# 5. Lancer l'orchestrateur MJ
python agents/gm_agent.py --session nouvelle
```
