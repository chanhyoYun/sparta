class Player:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.experience = 0
        self.power = power
        self.level = 1
        self.defense = 5

    # 플레이어_공격
    def attack(self, enemy):
        damage = self.power + (self.level * 2) - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            print(f"{self.name}이(가) {enemy.name}에게 {damage} 피해를 입혔습니다!")
        else:
            print(f"{self.name}의 공격은 {enemy.name}에게 아무런 효과가 없었습니다.")

    # 레벨업
    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 5
        print(f"{self.name}이 {self.level}으로 레벨업했습니다!")

    # 경험치 획득
    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.level * 10:


class Enemy:
    def __init__(self, name, level, hp, power, defense):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.defense = defense

    def attack(self, player):
        damage = self.power + (self.level * 0.5) - player.defense
        if damage > 0:
            player.hp -= damage
            print(f"{self.name}이(가) {player.name}에게 {damage} 피해를 입혔습니다!")
        else:
            print(f"{self.name}의 공격은 {player.name}에게 아무런 효과가 없었습니다.")

    def
