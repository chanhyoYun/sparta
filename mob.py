import random


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

    def show_status(self):
        print(f"{self.name}: HP {self.hp}/{self.max_hp}")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, 파워: {self.power})"


class Nomal_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'nomal'
        print(f'무속성 {self.name}')


class Water_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'water'

    def attack(self, other):
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.5))
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")


class Fire_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'fire'

    def attack(self, other):
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.5))
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")


class Grass_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'grass'

    def attack(self, other):
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.5))
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")


class Ground_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'ground'

    def attack(self, other):
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.5))
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")


class Ice_Monster(Monster):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attribute = 'ice'

    def attack(self, other):
        damage = random.randint(int(self.power * 0.8), int(self.power * 1.5))
        other.hp -= damage
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")


def generate_monster():
    monster_list = ['드래곤', '오크', '슬라임', '좀비', '고블린', '골렘',
                    '늑대인간', '미노타우르스', '메두사', '발록', '그리핀', '스켈레톤', '오우거']
    monster_name = random.choice(monster_list)
    monster_attribute_list = [Water_Monster, Fire_Monster,
                              Ground_Monster, Ground_Monster, Ice_Monster]

    monster_attribute = random.choice(monster_attribute_list)
    monster_hp = (random.randint(150, 200))
    monster_power = (random.randint(20, 25))
    monsters = monster_attribute(monster_name, monster_hp, monster_power)
    return monsters
