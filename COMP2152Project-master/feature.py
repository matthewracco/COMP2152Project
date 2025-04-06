import random
import functions_lab06_solution

# Additional Features Functions

def get_top_heroes(save_file="save.txt", top_n=3):
    hero_scores = {}
    try:
        with open(save_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("Hero") and "gained" in line:
                    parts = line.split()
                    hero_name = parts[1].lower()
                    stars = int(parts[-2])
                    hero_scores[hero_name] = hero_scores.get(hero_name, 0) + stars
        sorted_heroes = sorted(hero_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_heroes[:top_n]
    except FileNotFoundError:
        print("Save file not found.")
        return []

def show_top_heroes():
    print("    |    Here are the top heroes:")
    top_heroes = get_top_heroes()
    if not top_heroes:
        print("    |    No hero data found.")
    else:
        for i, (hero, stars) in enumerate(top_heroes, 1):
            print(f"    |    {i}. {hero.title()} - {stars} stars")

def show_feature():
    print("    ------------------------------------------------------------------")
    input("    |    Press Enter to show top 3 heroes")
    show_top_heroes()
    print("    ------------------------------------------------------------------")

# Main Game Function
def start_game():
    small_dice_options = list(range(1, 7))
    big_dice_options = list(range(1, 21))
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
    loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
    belt = []
    monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}
    num_stars = 0
    i = 0
    input_invalid = True

    while input_invalid and i in range(5):
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        combat_strength = input("Enter your combat Strength (1-6): ")
        print("    |", end="    ")
        m_combat_strength = input("Enter the monster's combat Strength (1-6): ")
        if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
            print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
            i += 1
            continue
        elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength) not in range(1, 7)):
            print("    |    Enter a valid integer between 1 and 6 only")
            i += 1
            continue
        else:
            input_invalid = False
            break

    if not input_invalid:
        combat_strength = int(combat_strength)
        m_combat_strength = int(m_combat_strength)
        input("Roll the dice for your weapon (Press enter)")
        print("    |    The hero's weapon is:", end=" ")
        weapon_roll = random.choice(small_dice_options)
        combat_strength = min(6, (combat_strength + weapon_roll))
        print(weapons[weapon_roll - 1])
        functions_lab06_solution.adjust_combat_strength(combat_strength, m_combat_strength)
        print("    ------------------------------------------------------------------")
        input("Analyze the Weapon roll (Press enter)")
        print("    |", end="    ")
        if weapon_roll <= 2:
            print("--- You rolled a weak weapon, friend")
        elif weapon_roll <= 4:
            print("--- Your weapon is meh")
        else:
            print("--- Nice weapon, friend!")
        if weapons[weapon_roll - 1] != "Fist":
            print("    |    --- Thank goodness you didn't roll the Fist...")

        input("Roll the dice for your health points (Press enter)")
        health_points = random.choice(big_dice_options)
        print("    |    Player rolled", health_points, "health points")

        input("Roll the dice for the monster's health points (Press enter)")
        m_health_points = random.choice(big_dice_options)
        print("    |    Monster has", m_health_points, "health points")

        print("    ------------------------------------------------------------------")
        print("    |    !!You find a loot bag!! You look inside to find 2 items:")
        input("Roll for first item (enter)")
        loot_options, belt = functions_lab06_solution.collect_loot(loot_options, belt)
        input("Roll for second item (Press enter)")
        loot_options, belt = functions_lab06_solution.collect_loot(loot_options, belt)
        belt.sort()
        print("    |    Your belt:", belt)

        belt, health_points = functions_lab06_solution.use_loot(belt, health_points)

        print("    ------------------------------------------------------------------")
        input("Analyze the roll (Press enter)")
        print("    |    --- You are matched in strength:", combat_strength == m_combat_strength)
        print("    |    --- You have a strong player:", (combat_strength + health_points) >= 15)

        input("Roll for Monster's Magic Power (Press enter)")
        power_roll = random.choice(list(monster_powers.keys()))
        m_combat_strength = min(6, m_combat_strength + monster_powers[power_roll])
        print("    |    The monster's combat strength is now", m_combat_strength, "using", power_roll)

        num_dream_lvls = -1
        while num_dream_lvls < 0 or num_dream_lvls > 3:
            input_val = input("    |    How many dream levels do you want to go down? (0-3): ")
            if not input_val.isdigit():
                print("Number entered must be a whole number between 0-3 inclusive, try again")
                continue
            num_dream_lvls = int(input_val)
            if 0 < num_dream_lvls <= 3:
                health_points -= 1
                crazy_level = functions_lab06_solution.inception_dream(num_dream_lvls)
                combat_strength += crazy_level
                print("combat strength:", combat_strength)
                print("health points:", health_points)

        print("    ------------------------------------------------------------------")
        print("    |    You meet the monster. FIGHT!!")
        while m_health_points > 0 and health_points > 0:
            input("Roll to see who strikes first (Press Enter)")
            attack_roll = random.choice(small_dice_options)
            if attack_roll % 2 != 0:
                input("You strike (Press enter)")
                m_health_points = functions_lab06_solution.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                    break
                input("The monster strikes (Press enter)!!!")
                health_points = functions_lab06_solution.monster_attacks(m_combat_strength, health_points)
                num_stars = 1 if health_points == 0 else 2
            else:
                input("The Monster strikes (Press enter)")
                health_points = functions_lab06_solution.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                    break
                input("The hero strikes!! (Press enter)")
                m_health_points = functions_lab06_solution.hero_attacks(combat_strength, m_health_points)
                num_stars = 3 if m_health_points == 0 else 2

        winner = "Hero" if m_health_points <= 0 else "Monster"

        tries = 0
        input_invalid = True
        while input_invalid and tries < 5:
            hero_name = input("Enter your Hero's name (in two words): ")
            name = hero_name.split()
            if len(name) != 2 or not all(part.isalpha() for part in name):
                print("    |    Please enter a valid alphabetical name with two parts.")
                tries += 1
            else:
                short_name = name[0][:2] + name[1][0]
                print("    |    I'm going to call you", short_name, "for short")
                input_invalid = False

        if not input_invalid:
            stars_display = "*" * num_stars
            print("    |    Hero", short_name, "gets <" + stars_display + "> stars")
            functions_lab06_solution.save_game(winner, hero_name=short_name, num_stars=num_stars)

# Entry Point
if __name__ == "__main__":
    while True:
        print("\n    --------------------- MAIN MENU ---------------------")
        print("    1. Start a new game")
        print("    2. Show top 3 heroes")
        print("    3. Exit")

        choice = input("    Enter your choice (1-3): ")

        if choice == '1':
            start_game()
        elif choice == '2':
            show_feature()
        elif choice == '3':
            print("    |    Thanks for playing! Goodbye!")
            break
        else:
            print("    |    Invalid choice. Please select 1-3.")
