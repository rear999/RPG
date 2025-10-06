import random

class Hiro:
    def __init__(self, health, damage, barrier):
        self.health = health
        self.damage = damage
        self.base_barrier = barrier  # Сохраняем базовое значение барьера
        self.current_barrier = barrier  # Текущее значение барьера

    def attack(self, enemy):
        critical_hit = random.random() < 0.1  # 10% шанс на критический удар
        damage_dealt = self.damage * (2 if critical_hit else 1)
        enemy.take_damage(damage_dealt)
        return damage_dealt

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.current_barrier)
        self.health -= damage_taken

    def end_turn(self):
        # Восстанавливаем барьер в конце раунда
        self.current_barrier = self.base_barrier