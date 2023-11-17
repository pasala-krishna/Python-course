import random

# Player's initial stats
player_name = input("Enter your character's name: ")
player_health = 100
player_attack = 10
player_gold = 0
inventory = []

# Initial game setup
enemies = [
    {"name": "Goblin", "health": 30, "attack": 5, "loot": "Gold"},
    {"name": "Dragon", "health": 100, "attack": 15, "loot": "Sword"},
    {"name": "Witch", "health": 50, "attack": 10, "loot": "Health Potion"},
]

locations = [
    {"name": "Village", "description": "A peaceful village where you can rest and buy supplies."},
    {"name": "Forest", "description": "A dark forest with hidden dangers."},
    {"name": "Cave", "description": "A mysterious cave with treasures and monsters."},
]

def display_stats():
    print(f"\nName: {player_name}")
    print(f"Health: {player_health}")
    print(f"Attack: {player_attack}")
    print(f"Gold: {player_gold}")
    print("Inventory: ", inventory)

def battle( enemy):
    global player_health, player_attack, player_gold, inventory
    while player_health > 0 and enemy["health"] > 0:
        print(f"\nYou encounter a {enemy['name']}!")
        print(f"{player_name}'s Health: {player_health}, {enemy['name']}'s Health: {enemy['health']}")
        action = input("Do you want to attack the enemy? (yes/no): ")
        
        if action.lower() == "yes":
            damage = random.randint(1, player_attack)
            enemy["health"] -= damage
            print(f"You attack the {enemy['name']} for {damage} damage.")
            
            if enemy["health"] <= 0:
                print(f"You defeated the {enemy['name']}!")
                if enemy['name'] == 'Goblin':
                    player_attack += 5
                    print(f'\nyour attak power incremented by 5')
                elif enemy['name'] == 'Witch':
                    player_attack += 10
                    print(f'\nyour attak power incremented by 10')
                elif enemy['name'] == 'Dragon':
                    player_attack += 15
                    print(f'\nyour attak power incremented by 15')
                loot = enemy["loot"]
                print(f"\nYou found {loot} in the {enemy['name']}'s remains.")
                if loot == "Gold":
                    player_gold += 10
                else:
                    inventory.append(loot)
                break
            
            damage = random.randint(1, enemy["attack"])
            player_health -= damage
            print(f"The {enemy['name']} attacks you for {damage} damage.")
            print(f"{player_name}'s Health: {player_health}, {enemy['name']}'s Health: {enemy['health']}")
        else:
            print("You decide to flee the battle.")
            break

# Main game loop
print(f"Welcome, {player_name}, to the Text RPG Game!")
while player_health > 0:
    display_stats()
    print("\nLocations:")
    for i, location in enumerate(locations):
        print(f"{i + 1}. {location['name']} - {location['description']}")
    choice = input("Choose a location (1/2/3): ")
    if choice == "1":
        print("You visit the Village. You can rest and buy supplies here.")
        player_health = 100
    elif choice == "2":
        print("You venture into the Forest.")
        enemy = random.choice(enemies)
        battle(enemy)
    elif choice == "3":
        print("You explore the Cave.")
        enemy = random.choice(enemies)
        battle(enemy)
    else:
        print("Invalid choice. Try again.")
if player_health <= 0:
    print(f"{player_name} was defeated. Game over!")
