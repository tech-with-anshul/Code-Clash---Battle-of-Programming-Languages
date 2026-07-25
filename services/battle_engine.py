import random

LANGUAGE_STATS = {
    "python": {"hp": 100, "attack": 25, "defense": 15, "speed": 10, "moves": ["TensorFlow Blast", "Pandas Storm", "NumPy Punch"]},
    "java": {"hp": 120, "attack": 20, "defense": 25, "speed": 12, "moves": ["Spring Boot Slam", "Garbage Collection", "Enterprise Shield"]},
    "javascript": {"hp": 90, "attack": 28, "defense": 12, "speed": 20, "moves": ["Async Attack", "Promise Chain", "Callback Hell"]},
    "typescript": {"hp": 100, "attack": 26, "defense": 18, "speed": 18, "moves": ["Type Assertion", "Interface Strike", "Strict Null Check"]},
    "c": {"hp": 110, "attack": 30, "defense": 20, "speed": 25, "moves": ["Pointer Attack", "Segmentation Fault", "Malloc Strike"]},
    "cpp": {"hp": 115, "attack": 32, "defense": 22, "speed": 22, "moves": ["Zero Cost Abstraction", "Memory Cannon", "Template Metaprogramming"]},
    "csharp": {"hp": 115, "attack": 24, "defense": 22, "speed": 15, "moves": ["LINQ Query", "Unity Blast", "CLR Execution"]},
    "go": {"hp": 105, "attack": 22, "defense": 20, "speed": 28, "moves": ["Goroutine Rush", "Concurrency Storm", "Channel Block"]},
    "rust": {"hp": 110, "attack": 25, "defense": 30, "speed": 20, "moves": ["Borrow Checker", "Ownership Lock", "Memory Shield"]},
    "ruby": {"hp": 95, "attack": 24, "defense": 14, "speed": 16, "moves": ["Rails Express", "Gem Install", "Method Missing"]},
    "php": {"hp": 100, "attack": 22, "defense": 16, "speed": 14, "moves": ["Legacy Punch", "WordPress Army", "Laravel Magic"]},
    "swift": {"hp": 105, "attack": 26, "defense": 20, "speed": 18, "moves": ["Apple Ecosystem", "Xcode Strike", "Optional Binding"]}
}

DOMAIN_MULTIPLIERS = {
    "ai": {"python": 1.5, "cpp": 1.2, "rust": 1.1},
    "web": {"javascript": 1.5, "typescript": 1.4, "php": 1.3, "ruby": 1.2, "python": 1.1},
    "systems": {"c": 1.5, "cpp": 1.5, "rust": 1.5, "go": 1.2},
    "enterprise": {"java": 1.5, "csharp": 1.5, "cpp": 1.2, "go": 1.2},
    "mobile": {"swift": 1.5, "java": 1.4, "javascript": 1.2, "csharp": 1.2}
}

def _do_attack(attacker, defender, turn, is_final_chance=False):
    """Simulate one attack. Returns a log entry dict."""
    move = random.choice(attacker["moves"])
    
    # Dodge chance based on defender speed (faster = more dodges)
    dodge_chance = min(0.25, defender["speed"] / 100.0)
    # Block chance based on defender defense
    block_chance = min(0.20, defender["defense"] / 120.0)
    
    roll = random.random()
    
    if roll < dodge_chance and not is_final_chance:
        # Defender dodged
        return {
            "turn": turn,
            "attacker": attacker["id"],
            "defender": defender["id"],
            "move": move,
            "result": "dodge",
            "damage": 0,
            "defender_hp": defender["hp"]
        }
    elif roll < dodge_chance + block_chance and not is_final_chance:
        # Defender blocked - takes reduced damage
        damage = max(2, int((attacker["attack"] - defender["defense"] * 0.7) * 0.3) + random.randint(-1, 1))
        defender["hp"] -= damage
        return {
            "turn": turn,
            "attacker": attacker["id"],
            "defender": defender["id"],
            "move": move,
            "result": "block",
            "damage": damage,
            "defender_hp": max(0, defender["hp"])
        }
    else:
        # Clean hit
        damage = max(5, attacker["attack"] - int(defender["defense"] * 0.5) + random.randint(-3, 3))
        defender["hp"] -= damage
        return {
            "turn": turn,
            "attacker": attacker["id"],
            "defender": defender["id"],
            "move": move,
            "result": "hit",
            "damage": damage,
            "defender_hp": max(0, defender["hp"])
        }


def simulate_battle(lang1_id, lang2_id, domain):
    p1_base = LANGUAGE_STATS.get(lang1_id, LANGUAGE_STATS["python"])
    p2_base = LANGUAGE_STATS.get(lang2_id, LANGUAGE_STATS["python"])
    
    # Apply domain multipliers
    m1 = DOMAIN_MULTIPLIERS.get(domain, {}).get(lang1_id, 1.0)
    m2 = DOMAIN_MULTIPLIERS.get(domain, {}).get(lang2_id, 1.0)
    
    p1 = {
        "id": lang1_id,
        "hp": int(p1_base["hp"] * m1),
        "max_hp": int(p1_base["hp"] * m1),
        "attack": int(p1_base["attack"] * m1),
        "defense": int(p1_base["defense"] * m1),
        "speed": int(p1_base["speed"] * m1),
        "moves": p1_base["moves"]
    }
    
    p2 = {
        "id": lang2_id,
        "hp": int(p2_base["hp"] * m2),
        "max_hp": int(p2_base["hp"] * m2),
        "attack": int(p2_base["attack"] * m2),
        "defense": int(p2_base["defense"] * m2),
        "speed": int(p2_base["speed"] * m2),
        "moves": p2_base["moves"]
    }
    
    battle_log = []
    
    turn = 1
    while p1["hp"] > 0 and p2["hp"] > 0:
        # Determine who goes first this turn based on speed + some randomness
        if p1["speed"] + random.randint(-5, 5) >= p2["speed"] + random.randint(-5, 5):
            first, second = p1, p2
        else:
            first, second = p2, p1
            
        # First attacks
        is_final = second["hp"] <= first["attack"] * 1.2  # near-death, no dodge allowed
        entry = _do_attack(first, second, turn, is_final_chance=is_final)
        battle_log.append(entry)
        
        if second["hp"] <= 0:
            break
            
        # Second attacks
        is_final = first["hp"] <= second["attack"] * 1.2
        entry = _do_attack(second, first, turn, is_final_chance=is_final)
        battle_log.append(entry)
        
        turn += 1
        
    winner = p1["id"] if p1["hp"] > 0 else p2["id"]
    
    return {
        "winner": winner,
        "p1_stats": {"max_hp": p1["max_hp"]},
        "p2_stats": {"max_hp": p2["max_hp"]},
        "log": battle_log
    }

