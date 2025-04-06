# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot (Elemental Shield added here)
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves", "Elemental Shield"]
belt = []

# DEMO MODE: Force Elemental Shield into belt for presentation
DEMO_MODE = True
if DEMO_MODE and "Elemental Shield" not in belt:
    belt.append("Elemental Shield")


# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}
special_attacks = [
    {"name": "Final Slash", "condition": 0.35, "damageBoost": 5},
    {"name": "Second Chance", "condition": 0.30, "healPoint": 10}
]
special_attack_used = False
# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
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

    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    belt, health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # ---------------------- Elemental Shield Feature ----------------------
    shield_activated = False
    if "Elemental Shield" in belt:
        print("    ------------------------------------------------------------------")
        print("    |    You possess the Elemental Shield! Rolling to see if it activates...")
        if random.choice([True, False]):
            print("    |    🛡️ Elemental Shield activates! The monster's magic is nullified!")
            m_combat_strength = max(1, m_combat_strength)
            shield_activated = True
        else:
            print("    |    Elemental Shield failed to activate.")
    # ----------------------------------------------------------------------

    if not shield_activated:
        m_combat_strength += min(6, monster_powers[power_roll])
        print("    |    The monster's combat strength is now " + str(m_combat_strength) + " using the " + power_roll + " magic power")
    else:
        print("    |    The monster's magic power (" + power_roll + ") has no effect.")

    # Continue with the rest of the original game code...
    # (no changes needed for fight sequence, special attacks, etc.)
