# feature.py
import random


def random_chance_event():
    """
    Triggers a random event after winning a battle.
    Returns a tuple of (health_change, message, items)
    """
    event_type = random.choice(["health", "damage", "loot", "nothing"])

    if event_type == "health":
        health_gain = random.randint(1, 5)
        return (health_gain, f"You found a healing spring! Gained {health_gain} health.", [])

    elif event_type == "damage":
        damage = random.randint(1, 3)
        return (-damage, f"Oh no! You stepped on a trap and lost {damage} health.", [])

    elif event_type == "loot":
        loot_options = ["Health Potion", "Golden Ring", "Magic Dust"]  # Using existing item names
        loot = random.choice(loot_options)
        return (0, f"You discovered {loot}!", [loot])

    else:
        return (0, "The battle leaves you exhausted but otherwise unchanged.", [])