from time import sleep
import random


class Character:
    def __init__(self, name, hp, power, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"{other.name}의 남은 HP가 {other.hp}입니다.")

    def show_status(self, other):
        print(
            f"{other.name}의 상태: HP {other.hp}/{other.max_hp} MP {other.mp}/{other.max_mp}")


class Players(Character):
    def __init__(self, name, hp, power, mp):
        super().__init__(name, hp, power, mp)

    def magic(self, other):
        use_mp = 30  # random.randint(other.max_mp - 10, other.max_mp)
        if other.mp >= use_mp:
            damage = random.randint(self.power - 2, self.power + 2) + 15
            other.hp = max(other.hp - damage, 0)

            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            other.mp = other.max_mp - use_mp

            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")
            else:
                print(f"{other.name}이(가) {other.hp}이 되었습니다.")
        else:
            print(f"{self.name}의 MP가 부족하여 턴이 넘어갑니다.")


class Monster(Character):
    def __init__(self, name, hp, power, mp):
        super().__init__(name, hp, power, mp)

    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


def playertrun():
    print("\n------------------플레이어 턴------------------")
    commend = input("1 공격 또는 2 마법 : ")
    if commend == "1":
        player.attack(monster)
    elif commend == "2":
        player.magic(monster)
    else:
        print("잘못 입력하여 턴이 넘어갑니다.")
    return monster


def monsterturn():
    print("\n------------------몬스터 턴------------------")
    # sleep(3)
    monster.attack(player)
    return player


def status():
    print("\n-------------------상태창---------------------")
    print(f"{player.name} : 공격데미지 {player.power} / 마법데미지 {player.power + 15}")
    player.show_status(player)
    monster.show_status()


def monster_die():
    if monster.hp <= 0:
        return True
    else:
        return False


def player_die():
    if player.hp <= 0:
        return True
    else:
        return False


def setting():
    # 플레이어 설정
    # print("Plyer 이름을 입력한 뒤 ENTER 입력해주세요.")
    player_name = input()
    player_name = "1234"
    player_hp = random.randint(100, 120)
    player_power = random.randint(20, 30)
    player_mp = random.randint(20, 25)
    player = Players(player_name, player_hp, player_power, player_mp)

    # 몬스터 설정
    monster_name = "JELLO"
    monster_hp = random.randint(80, 100)
    manster_power = random.randint(15, 25)
    manster_mp = 5
    monster = Monster(monster_name, monster_hp, manster_power, manster_mp)

    return player, monster


# 게임 실행 부분
player, monster = setting()
# sleep(1)

while True:
    status()
    monster = playertrun()
    # sleep(1)
    mob_end = monster_die()
    if mob_end:
        print("\n몬스터가 죽었습니다.")

    player = monsterturn()
    play_end = player_die()
    if play_end:
        print("\n패배!!!")
        break
