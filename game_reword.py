import test
import random
import time


def reward():
    player_info = test.Player()
    name = player_info.name
    # hp = player_info.hp
    # max_hp = player_info.max_hp
    # power = player_info.power
    # experience = player_info.experience
    while True:
        print("몬스터 처치 성공! \n다음 층으로 올라갑니다.\n올라가기 전에 보상을 선택해 주세요.")
        print('1. 체력회복 2. 마나회복 3. 경험치 획득 4. 아이템 획득 5.???(랜덤)')
        select = int(input("→   "))

        # reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
        # choice = reward_list(select())
        # print(choice)

        # print(f"선택된 보상은 {select} 입니다.")

        if (select == 1):
            # Monster.hp 50% 회복
            # player_info.name += 150
            print(f"{name}님의 체력이 50% 회복되었습니다.\n현재 HP {hp}/{max_hp}")
            time.sleep(2)

            # return charge_hp.rest()

            break

        elif (select == 2):
            # Player.power 100% 회복
            # self.power = 200
            print(f"{name}님의 MP가 전체 회복되었습니다.\n현재 MP {power:200}")
            time.sleep(2)

            break
            # return test.py의 Player.power = max_hp

        elif (select == 3):
            # Player.경험치 40 획득(몬스터 3마리 잡고 올라갈때 경험치 40만큼 부여 -> )
            # self.experience += 40
            print(f"{name}님은 경험치 40을 획득했습니다.\n현재 경험치 {experience}")
            time.sleep(2)

            break
            # return test.py의 self.experience += 40

        elif (select == 4):
            # 아이템 획득
            # 아이템 시스템으로 연결
            # item()함수 or 클래스로 연결
            print(f"{name}님은 아이템 으로 연결됩니다.")
            # 아이템 함수 호출
            time.sleep(2)

            break
            # return item.py의 item 선택으로 연결

        elif (select == 5):
            reward_list = ['체력회복', '마나회복', '경험치획득', '아이템획득']
            choice = random.choice(reward_list)
            print(choice)
            print(f"선택된 보상은 {choice} 입니다.")
            for index, value in enumerate(reward_list):
                a = list(print(index, value))

            time.sleep(2)
        # return
        #     # return select == num
        #
        #     # return select == (num)
        else:
            print("적용되지 않은 값입니다. \n다시선택해주세요")
            time.sleep(1)

            break
#
#         # return 선택된 num값의 if 문으로
