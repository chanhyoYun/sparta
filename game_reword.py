import time
import random

player = Player(player_name, player_hp, player_mp, player_power)
# ===============================유혜민 보상 시스템===========


def reward():
    # player_info = player
    # name = player_info.name
    # hp = player_info.hp
    # max_hp = player_info.max_hp
    # power = player_info.power
    # experience = player_info.experience
    player = Player()
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
            # player.max_hp 300 += player.max_hp / 2

            print(f"{player.name}님의 체력이 50% 회복되었습니다.\n현재 HP {player.hp}")
            time.sleep(2)

            # return charge_hp.rest()

            break

        elif (select == 2):
            # player_mp 100% 회복
            player_mp = 20

            print(f"{player.name}님의 MP가 전체 회복되었습니다.\n현재 MP {player.mp}")
            time.sleep(2)

            break
            # return test.py의 Player.power = max_hp

        elif (select == 3):
            # Player.경험치 40 획득(몬스터 3마리 잡고 올라갈때 경험치 40만큼 부여 -> )
            Player.experience += 40
            print(f"{player.name}님은 경험치 40을 획득했습니다.\n현재 경험치 {player.experience}")
            time.sleep(2)

            break
            # return test.py의 self.experience += 40

        elif (select == 4):

            # 아이템 상점이동

            # 아이템 시스템으로 연결

            # item()함수 or 클래스로 연결

            item = {"1": '강철검', "2": '철갑옷', "3": 'HP포션', "4": 'MP포션'}

            k, item_choice = random.choice(list(item.items()))

            print(f"{player.name}님은 {item_choice}을 뽑으셨습니다.")

            if k == "1":

                return sword()

            elif k == "2":

                return armor()

            elif k == "2":

                return potion()

            else:

                return potion2()

            time.sleep(2)

            break
            # return item.py의 item 선택으로 연결

        elif (select == 5):

            reward = {"1": '체력회복', "2": '마나회복', "3": '경험치획득', "4": '아이템획득'}

            k, reward_choice = random.choice(list(reward.items()))

            print(reward_choice)

            item_select = int(k)

            print(f"선택된 보상은 {reward_choice} 입니다.")

            if (item_select == 1):

                # player.hp += player.max_hp / 2

                player.hp += player.max_hp / 2

                print(f"{player.name}님의 체력이 50% 회복되었습니다.\n현재 HP {player.hp}")
                time.sleep(2)

                break

            elif (item_select == 2):

                # player_mp = 20

                print(f"{player.name}님의 MP가 전체 회복되었습니다.\n현재 MP {player.mp}")
                time.sleep(2)

                break

            elif (item_select == 3):

                # experience += 40

                Player.experience += 40
                print(f"{player.name}님은 경험치 40을 획득했습니다.\n현재 경험치 {player.experience}")
                time.sleep(2)

                break

            elif (item_select == 4):

                # 아이템 획득

                # 아이템 시스템으로 연결

                # item()함수 or 클래스로 연결

                item = {"1": '강철검', "2": '철갑옷', "3": 'HP포션', "4": 'MP포션'}

                k, item_choice = random.choice(list(item.items()))

                print(f"{player.name}님은 {item_choice}을 뽑으셨습니다.")

                if k == "1":

                    return sword()

                elif k == "2":

                    return armor()

                elif k == "2":

                    return potion()

                else:

                    return potion2()

                time.sleep(2)

        # return
        #     # return select == num
        #
        #     # return select == (num)
        else:
            print("적용되지 않은 값입니다. \n다시선택해주세요")
            time.sleep(1)

            break


# ================================game_reward.py
