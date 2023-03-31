import random
import items
from time import sleep
import os

# 보상 함수


class Reward:
    def __init__(self):
        pass

    def strength_up(self):
        self.job_str += 2
        self.skill_power += 2
        print("힘(Strength)이 2증가하였습니다.")
        sleep(0.5)

    def intelligence_up(self):
        self.job_int += 2
        self.skill_power += 2
        print("지능(Intelligence)이 2증가하였습니다.")
        sleep(0.5)

    def agility_up(self):
        self.job_agi += 2
        self.skill_power += 2
        print("민첩(Agility)이 2증가하였습니다.")
        sleep(0.5)

    def health_up(self):
        self.hp += 30
        self.max_hp += 30
        print("체력(Health)이 30증가하였습니다.")
        sleep(0.5)

    def agility_up(self):
        self.mp += 10
        self.max_mp += 10
        print("마나(Mana)이 10증가하였습니다.")
        sleep(0.5)


def rewards(player):

    print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요.")
    while True:
        print("1. 스탯 증가")
        print("2. 아이템 획득")
        print("3. 랜덤선택")
        reward_choice = input("→   ")
        sleep(0.5)
        os.system('cls')
        if reward_choice == "1":
            print("증가할 스탯을 선택해주세요.")
            print("1. 힘(Strength)")
            print("2. 지능(Intelligence)")
            print("3. 민첩(Agility)")
            print("4. 체력(Health)")
            print("5. 마나(Mana)")
            stats_choice = input("→   ")
            sleep(0.5)
            os.system('cls')
            if stats_choice == "1":
                Reward.strength_up(player)
            elif stats_choice == "2":
                Reward.intelligence_up(player)
            elif stats_choice == "3":
                Reward.agility_up(player)
            elif stats_choice == "4":
                Reward.agility_up(player)
            elif stats_choice == "5":
                Reward.agility_up(player)

        elif reward_choice == "2":
            item_store = items.make_item()
            item_in = random.choice(item_store)
            player.inventory.append(item_in.name)
            print(f"{item_in.name}을 얻었습니다.")

        elif reward_choice == "3":
            reward_choice = random.randint(1, 2)
            if reward_choice == 1:
                print("스탯 증가가 선택되었습니다.")

                stats_choice = random.randint(1, 5)
                if stats_choice == 1:
                    Reward.strength_up(player)
                elif stats_choice == 2:
                    Reward.intelligence_up(player)
                elif stats_choice == 3:
                    Reward.agility_up(player)
                elif stats_choice == 4:
                    Reward.agility_up(player)
                elif stats_choice == 5:
                    Reward.agility_up(player)

            elif reward_choice == 2:
                print("아이템이 랜덤으로 선택됩니다.")
                sleep(0.5)
                item_store = items.make_item()
                item_in = random.choice(item_store)
                player.inventory.append(item_in.name)
                print(f"{item_in.name}을 얻었습니다.")
        else:
            print("다시 선택해주세요.")
            continue

        os.system('cls')
