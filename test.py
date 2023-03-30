import mob
import job


# 게임 실행 함수
def main():
    print("잡아보자...!")
    player = job.create_player()
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
            monster = mob.generate_monster()
            print(f"몬스터 {monster.name} 등장!")
            while monster.is_alive():
                print("-" * 20)
                print(f"{monster}")
                print(f"{player}")
                print("뭐할래?")
                print("1. 공격")
                print("2. 스킬")
                print("3. 포션사용")
                print("4. 도망")
                battle_choice = input("> ")
                if battle_choice == "1":
                    player.attack(monster)
                    if monster.is_alive():
                        monster.attack(player)
                        if not player.is_alive():
                            print("패배!")
                            quit()
                elif battle_choice == "2":
                    player.skill_attack(monster)
                    if monster.is_alive():
                        monster.attack(player)
                elif battle_choice == "3":
                    player.heal()
                    monster.attack(player)
                elif battle_choice == "4":
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
