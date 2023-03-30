import random
import tower

towerfile = tower.generate_monster()

# 모체 클래스


class Object:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        other.hp -= self.power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, 파워: {self.power})"

# 플레이어 설정


class Player(Object):
    def __init__(self):
        self.name = "somsom"
        self.level = 1
        self.experience = 0
        self.max_hp = 20
        self.hp = self.max_hp
        self.power = 5
        self.inventory = []

    def attack(self, monster):
        monster.hp -= self.power
        print(f"{self.name}이 {monster.name}에게 {self.power} 피해를 입혔습니다.")
        if not monster.is_alive():
            print(f"{monster.name} 가 죽었어요..!")
            self.experience += 10
            self.level_up()

    def level_up(self):
        if self.experience >= self.level * 20:
            self.level += 1
            self.max_hp += 5
            self.hp = self.max_hp
            self.power += 2
            print(f"레벨업 했습니다: {self.level}!")

    def heal(self):
        if "Potion" in self.inventory:
            self.hp += 5
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.inventory.remove("Potion")
            print("포션을 사용했습니다.")
        else:
            print("포션을 가지고 있지 않아요!")

    def rest(self):
        self.hp = self.max_hp
        print("휴식 후 모든 체력 회복!")

    def view_stats(self):
        print(f"레벨: {self.level}")
        print(f"경험치: {self.experience}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"파워: {self.power}")
        print(f"인벤토리: {', '.join(self.inventory)}")


# def generate_monster():
#     monster_names = ["Slime", "Goblin", "Skeleton"]
#     monster_name = random.choice(monster_names)
#     monster_hp = random.randint(5, 15)
#     monster_power = random.randint(2, 5)
#     return Object(monster_name, monster_hp, monster_power)


# 게임 실행 함수
def main():
    print("잡아보자...!")
    player = Player()
    while True:
        print("=" * 20)
        print("무엇을 선택하시겠나요?")
        print("1. 모험")
        print("2. 포션 사용")
        print("3. 휴식")
        print("4. 상태창 보기")
        print("5. Quit")
        choice = input("> ")
        if choice == "1":
            monster = towerfile
            print(f"몬스터 {monster.name} 등장!")
            while monster.is_alive():
                print("-" * 20)
                print(f"{monster}")
                print(f"{player}")
                print("뭐할래?")
                print("1. 공격")
                print("2. 포션사용")
                print("3. 도망")
                battle_choice = input("> ")
                if battle_choice == "1":
                    player.attack(monster)
                    if monster.is_alive():
                        monster.attack(player)
                        if not player.is_alive():
                            print("패배!")
                            quit()
                elif battle_choice == "2":
                    player.heal()
                    monster.attack(player)
                elif battle_choice == "3":
                    print("도망간다.")
                    break
        elif choice == "2":
            player.heal()
        elif choice == "3":
            player.rest()
        elif choice == "4":
            player.view_stats()
        elif choice == "5":
            quit()


# 실행
main()
