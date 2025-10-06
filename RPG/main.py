from Enemy import Enemy
from Hiro import Hiro

def display_health(enemies):
    for i, enemy in enumerate(enemies):
        print(f"Enemy {i + 1} Health: {enemy.health}")

def battle(hero, enemies):
    while hero.health > 0 and any(enemy.health > 0 for enemy in enemies):
        print(f"\nHero's Health: {hero.health}")
        display_health(enemies)

        for enemy in enemies:
            if enemy.health > 0:
                action = input("Choose action: (1) Attack (2) Defend: ")
                if action == "1":
                    damage = hero.attack(enemy)
                    print(f"Hero attacks {enemy.__class__.__name__} for {damage} damage!")
                elif action == "2":
                    print("Hero defends!")
                
                if enemy.health > 0:
                    enemy.attack(hero)
                    print(f"{enemy.__class__.__name__} attacks Hero for {enemy.damage} damage!")

        # Восстанавливаем барьер после каждого раунда
        hero.end_turn()

    if hero.health <= 0:
        print("Hero has fallen...")
    else:
        print("Enemies have been defeated!")

if __name__ == "__main__":
    hiro = Hiro(1000, 72, 45)
    knight = Enemy(500, 75)
    knight2 = Enemy(450, 75)
    knight3 = Enemy(400, 75)
    
    battle(hiro, [knight, knight2, knight3])
