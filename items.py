import random


class Item:
    def __init__(self, name, price, isdropable):
        self.name = name
        self.price = price
        self.isdropable = isdropable

    def sale(self):
        print(f'[{self.name}] 판매 가격은 [{self.price}]')

    def discard(self):
        if self.isdropable:
            print(f'[{self.name}] 아이템을 버렸습니다.')
        else:
            print(f'[{self.name}] 아이템을 버릴 수 없습니다.')

    def __str__(self):
        return f"{self.name}를(을) 획득했습니다."


class WearableItem(Item):
    def __init__(self, name, price, isdropable, effect):
        super().__init__(name, price,  isdropable)
        self.effect = effect

    def wear(self):
        print(f'[{self.name}] 착용했습니다.{self.effect}')


class UsableItem(Item):
    def __init__(self, name, price, isdropable, effect):
        super().__init__(name, price, isdropable)
        self.effect = effect

    def use(self):
        print(f'[{self.name}] 사용했습니다.{self.effect}')


def items():
    sword = WearableItem('강철검', 30000, True, 'HP 50 증가, 공격력 10')
    armor = WearableItem('철갑옷', 50000, True, 'HP 100 증가, 마력 9000 증가')
    potion = UsableItem('HP포션', 1500000, False, 'HP 전부 회복')
    potion2 = UsableItem('MP포션', 1500000, False, 'MP 전부 회복')
    items = [sword, armor, potion, potion2]
    item = random.choice(items)
    return item


