import random
import items

# 보상 함수


class Reward:
    def __init__(self):
        pass

    def strength_up(self):
        self.job_str += 2
        self.skill_power += 2

    def intelligence_up(self):
        self.job_int += 2
        self.skill_power += 2

    def agility_up(self):
        self.job_agi += 2
        self.skill_power += 2

    def item_get(self):
        a = items.items()
        self.inventory.append(a)


def rewards(player):
    print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요.")
    print("1. 스탯 증가")
    print("2. 아이템 획득")
    print("3. 랜덤선택")
    reward_choice = input("→   ")
    if reward_choice == "1":
        print("증가할 스탯을 선택해주세요.")
        print("1. 힘(Strength)")
        print("2. 지능(Intelligence)")
        print("3. 민첩(Agility)")
        stat_choice = input("→   ")
        if stat_choice == "1":
            Reward.strength_up(player)
        elif stat_choice == "2":
            Reward.intelligence_up(player)
        elif stat_choice == "3":
            Reward.agility_up(player)

    elif reward_choice == "2":
        Reward.item_get(player)

    elif reward_choice == "3":
        reward_choice = random.randint(1, 3)
        if reward_choice == "1":
            print("증가할 스탯을 선택해주세요.")
            print("1. 힘(Strength)")
            print("2. 지능(Intelligence)")
            print("3. 민첩(Agility)")
            stat_choice = input("→   ")
            if stat_choice == "1":
                Reward.strength_up(player)
            elif stat_choice == "2":
                Reward.intelligence_up(player)
            elif stat_choice == "3":
                Reward.agility_up(player)

        elif reward_choice == "2":
            # 아이템과 연결해야 함
            pass
