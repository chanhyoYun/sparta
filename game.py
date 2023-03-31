import mob
import job
import mine
import items
from time import sleep
import os

# 게임 실행 함수


def main():
    while True:
        print("A-4 팀 프로젝트")
        print("타워에 올라갈수록 쌔지는 몬스터를 잡아보자 !")
        print("=" * 30)
        print(f"{player.tower_stage} 층입니다.")
        print("무엇을 선택하시겠나요?")
        print("1. 모험")
        print("2. 포션 사용")
        print("3. 휴식")
        print("4. 상태창 보기")
        print("5. 상점 이용")
        print("6. Quit")
        choice = input("> ")
        sleep(1)
        os.system('cls')
        if choice == "1":
            monster = mob.generate_monster()
            monster.hp += int(player.tower_stage * 10)
            monster.max_hp += int(player.tower_stage * 10)
            monster.power += int(player.tower_stage * 5)
            print(f"몬스터 {monster.name} 등장!")
            while monster.is_alive():
                print("=" * 25)
                print(f"{monster}")
                print(f"{player}")
                print("=" * 25)
                print("행동을 선택해주세요.")
                print("1. 공격")
                print("2. 스킬")
                print("3. 포션사용")
                print("4. 인벤토리 보기")
                print("5. 도망")
                battle_choice = input("> ")
                sleep(0.5)
                os.system('cls')
                if battle_choice == "1":
                    player.attack(monster)
                    sleep(0.5)
                    if monster.is_alive():
                        monster.attack(player)
                        sleep(0.5)
                        if not player.is_alive():
                            print(f"{player.name}이 죽었습니다.")
                            print(f"{player.tower_stage}층에서 게임이 종료됩니다.")
                            quit()
                    elif not monster.is_alive():
                        mine.rewards(player)
                elif battle_choice == "2":
                    player.skill_attack(monster)
                    if monster.is_alive():
                        monster.attack(player)
                        if not player.is_alive():
                            print(f"{player.name}이 죽었습니다.")
                            print(f"{player.tower_stage}층에서 게임이 종료됩니다.")
                            quit()
                elif battle_choice == "3":
                    player.heal()
                    monster.attack(player)
                elif battle_choice == "4":
                    print(f"인벤토리: {', '.join(player.inventory)}")
                    job.item_equip(player)
                elif battle_choice == "5":
                    print("도망간다.")
                    break
        elif choice == "2":
            player.heal()
            sleep(0.5)
            os.system('cls')
        elif choice == "3":
            player.rest()
            sleep(0.5)
            os.system('cls')
        elif choice == "4":
            player.view_stats()
            job.item_equip(player)
            sleep(0.5)
            os.system('cls')
        elif choice == "5":
            items.get_items(player)
            sleep(0.5)
            os.system('cls')
        elif choice == "6":
            print("게임이 종료됩니다.")
            quit()


# 실행
player = job.create_player()
main()
