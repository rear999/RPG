class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, hero):
        hero.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage