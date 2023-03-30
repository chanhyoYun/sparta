import random
import sys
import os

from level import *


class BaseCharacter:
    def __init__(self, name, hp, normal_power):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.normal_power = normal_power

    def normal_attack(self, target):
        print(f"{self.name}의 normal attack!")
        damage = random.randint(
            int(self.normal_power*0.8), int(self.normal_power*1.2))
        # target.hp = target.hp - 20
        target.current_hp -= damage
        print(f"{target.name}에게 {damage} 만큼의 데미지를 입혔습니다.")

        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌습니다. 게임을 종료합니다.")
            return

    def show_status(self):
        print(f"{self.name}의 정보 hp : {self.current_hp} / {self.max_hp}")
        # 상태 정보 출력


class Player(BaseCharacter):
    def __init__(self, name, hp, mp, normal_power, magic_power, exp):
        super().__init__(name, hp, normal_power)
        self.max_mp = mp
        self.current_mp = mp
        self.magic_power = magic_power
        self.player_exp_max = exp

    def magic_attack(self, target):
        print(f"{self.name}의 magic attack!")
        if self.current_mp - 20 < 0:
            print("마나가 부족해서 마법 공격을 하지 못했습니다.")
            return

        damage = random.randint(
            int(self.normal_power*0.7), int(self.normal_power*1.3))

        self.current_mp -= 20
        # target.hp = target.hp - 20
        target.current_hp -= damage
        print(f"{target.name}에게 {damage} 만큼의 데미지를 입혔습니다.")

        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌습니다. 게임을 종료합니다.")
            sys.exit()


class Monster(BaseCharacter):
    def __init__(self, name, hp, normal_power, exp):
        super().__init__(name, hp, normal_power)
        self.exp = exp


os.system("cls")
# player_name = input("이름을 입력해주세요 : ")
player_name = "test"
# level = input("몬스터 레벨을 선택해주세요(1 ~ 3) 0: 랜덤: ")
# monster_list = [
# Monster("슬라임", 100, 20),
# Monster("주황버섯", 200, 30),
# Monster("골렘", 300, 40),
# ]

# if level == "0":
# random.choice(monster_list)

# else:
# monster_dict = {str(i): x for i, x in enumerate(monster_list, 1)}
# monster = monster_dict[level]
# monster_dict = {
#     "1": Monster("슬라임", 100, 20),
#     "2": Monster("주황버섯", 200, 30),
#     "3": Monster("골렘", 300, 40),
# }

# Monster("랜덤몬스터", random.randint(50, 200), random.randint(10, 30))
# monster = monster_dict["level"]
player = Player(player_name, 100, 20, 20, 20, 20)
monster = Monster("슬라임", 100, 10, 10)

while True:
    player.show_status()
    monster.show_status()
    action = input("행동을 선택해주세요 / 1: 일반공격 / 2: 마법공격 / exit: 프로그램 종료\n")
    os.system("cls")

    if action == "1":
        player.normal_attack(monster)

    elif action == "2":
        player.magic_attack(monster)

    elif action == "exit":
        sys.exit()

    else:
        print("정확한 값을 입력해 주세요.")
        continue

    monster.normal_attack(player)
