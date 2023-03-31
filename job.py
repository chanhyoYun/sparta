import random


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

    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, 파워: {self.power})"

# 플레이어 설정


class Player(Object):
    def __init__(self, name, hp, power, mp):
        self.name = name
        self.level = 1
        self.experience = 0
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.money = 1000000
        self.power = power
        self.inventory = []
        self.job = create_job()
        self.job_name = self.job.job_name
        self.job_skill = self.job.job_skill
        self.job_str = self.job.strength
        self.job_int = self.job.intelligence
        self.job_agi = self.job.agility
        self.skill_power = self.job_str + self.job_int + self.job_agi
        self.skill_use_mp = self.skill_power // 2

    def attack(self, monster):
        monster.hp -= self.power
        print(f"{self.name}이(가) {monster.name}에게 {self.power} 피해를 입혔습니다.")
        if not monster.is_alive():
            print(f"{monster.name} 가 죽었어요..!")
            self.experience += 10
            self.money += 100
            self.level_up()

    def skill_attack(self, monster):
        if self.mp >= self.skill_use_mp:
            monster.hp -= self.skill_power
            self.mp -= self.skill_use_mp
            print(
                f"{self.name}이(가) {monster.name}에게 {self.job_skill}를(을) 사용하여 {self.skill_power} 피해를 입혔습니다.")
            if not monster.is_alive():
                print(f"{monster.name} 가 죽었음")
                self.experience += 10
                self.money += 100
                self.level_up()
        else:
            print(f"MP가 부족합니다. {self.mp}/{self.max_mp}")
            print(f"스킬 사용 마나 : {self.skill_use_mp}")
            print(f"스킬을 사용하지 못해 일반 공격합니다.")
            self.attack(monster)

    def level_up(self):
        print(f"{self.experience}경험치를 얻었습니다.")
        print(f"{self.name} 경험치: {self.experience}/{self.level * 20}")
        if self.experience >= self.level * 20:
            self.level += 1
            self.max_hp += 5
            self.max_mp += 5
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.power += 10
            self.experience = 0
            print(f"레벨업 했습니다: {self.level}!")

    def heal(self):
        print("1. HP 포션")
        print("2. MP 포션")
        potion_type = input(">  ")
        if potion_type == "1":
            if "potion" in self.inventory:
                self.hp += 5
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
                self.inventory.remove("potion")
                print("포션을 사용했습니다.")
            else:
                print("포션을 가지고 있지 않아요!")

        elif potion_type == "2":
            if "potion2" in self.inventory:
                self.mp += 5
                if self.mp > self.max_mp:
                    self.mp = self.max_mp
                self.inventory.remove("potion2")
                print("포션을 사용했습니다.")
            else:
                print("포션을 가지고 있지 않아요!")

    def rest(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        print("휴식 후 모든 체력, 마나 회복!")

    def view_stats(self):
        print(f"레벨: {self.level}")
        print(f"직업: {self.job_name}")
        print(f"경험치: {self.experience}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"MP: {self.mp}/{self.max_mp}")
        print(f"Gold: {self.money}")
        print(f"파워: {self.power}")
        print(f"스킬파워: {self.skill_power}")
        print(f"인벤토리: {', '.join(self.inventory)}")
        print("----------------------------------------------")
        print(f"힘(Strength): {self.job_str}")
        print(f"지능(Intelligence): {self.job_int}")
        print(f"민첩(Agility): {self.job_agi}")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, 파워: {self.power}, 스킬파워: {self.skill_power})"


class Job(Player):
    def __init__(self):
        self.job_name = "직업이름"
        self.strength = 7  # 스탯 힘
        self.intelligence = 7  # 스탯 지능
        self.agility = 7  # 스탯 민첩

    def __str__(self):
        return f"{self.job_name}(으)로 선택했습니다."


class Warrior(Job):
    def __init__(self):
        self.job_name = "전사"
        self.strength = 10
        self.intelligence = 5
        self.agility = 7
        self.job_skill = "파워스크라이크"

        #     self.strength = job.strength + 3
        #     self.intelligence = job.intelligence - 2
        #     self.agility = job.agility + 2


class Archer(Job):
    def __init__(self):
        self.job_name = "궁수"
        self.strength = 7
        self.intelligence = 10
        self.agility = 5
        self.job_skill = "홀리애로우"

        #     self.strength = job.strength - 2
        #     self.intelligence = job.intelligence + 3
        #     self.agility = job.agility + 2


class Wizard(Job):
    def __init__(self):
        self.job_name = "마법사"
        self.strength = 5
        self.intelligence = 10
        self.agility = 7
        self.job_skill = "썬더볼트"

        #     self.strength = job.strength - 2
        #     self.intelligence = job.intelligence + 3
        #     self.agility = job.agility + 2


class Thief(Job):
    def __init__(self):
        self.job_name = "도적"
        self.strength = 7
        self.intelligence = 7
        self.agility = 10
        self.job_skill = "쿼드스로우"

        #     self.strength = job.strength + 1
        #     self.intelligence = job.intelligence + 1
        #     self.agility = job.agility + 3

# 플레이어 생성


def create_player():
    player_name = input("플레이어 이름을 입력해주세요: ")
    player_hp = random.randint(150, 200)
    player_mp = random.randint(50, 60)
    player_power = random.randint(25, 30)
    players = Player(player_name, player_hp, player_power, player_mp)
    return players

# 직업 선택, 생성


def create_job():
    print("직업을 선택해주세요")
    print("1. 전사(Warrior)")
    print("2. 궁수(Archer)")
    print("3. 마법사(Wizard)")
    print("4. 도적(Thief)")
    job_choice = input("> ")
    if job_choice == "1":
        player_job = Warrior()
        print(f"{player_job}")
    elif job_choice == "2":
        player_job = Archer()
        print(f"{player_job}")
    elif job_choice == "3":
        player_job = Wizard()
        print(f"{player_job}")
    elif job_choice == "4":
        player_job = Thief()
        print(f"{player_job}")
    return player_job
