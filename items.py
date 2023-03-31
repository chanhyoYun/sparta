class Item:
    def __init__(self, item_num, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
        self.item_num = item_num

    def show_item(self):
        print(f'{self.item_num} {self.name} {self.price} {self.weight}')

    def sale(self):
        print(f'[{self.name}] 판매 가격은 [{self.price}]')

    def discard(self):
        if self.isdropable:
            print(f'[{self.name}] 아이템을 버렸습니다.')
        else:
            print(f'[{self.name}] 아이템을 버릴 수 없습니다.')

    def __str__(self):
        return f'{self.name}'


class WearableItem(Item):
    def __init__(self, item_num, name, price, weight, isdropable, effect):
        super().__init__(item_num, name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f'[{self.name}] 착용했습니다.{self.effect}')


class UsableItem(Item):
    def __init__(self, item_num, name, price, weight, isdropable, effect):
        super().__init__(item_num, name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f'[{self.name}] 사용했습니다.{self.effect}')


def make_item():
    sword = WearableItem(1, '강철검', 30000, 3.5, True, '체력 50 증가, 마력 3000 증가')
    armor = WearableItem(2, '철갑옷', 50000, 3.5, True, 'HP 50 증가, 마력 9000 증가')
    potion = UsableItem(3, 'HP포션', 1500000, 0.1, False, '효과 300초 지속 전부회복')
    potion2 = UsableItem(4, 'MP포션', 1500000, 0.1, False, '효과 300초 지속 전부회복')
    save_item = [sword, armor, potion, potion2]
    return save_item


def get_items(player):
    store = make_item()
    for i in range(len(store)):
        print(f"{store[i].item_num}. {store[i].name}, 가격: {store[i].price}")
    choice = input("> ")
    if player.money >= store[0].price and choice == "1":
        player.inventory.append(store[0].name)
        player.money -= store[0].price

        print(f'{store[0].name}을 구매했습니다.')

    elif player.money >= store[1].price and choice == "2":
        player.inventory.append(store[1].name)
        player.money -= store[1].price

        print(f'{store[1].name}을 구매했습니다.')

    elif player.money >= store[2].price and choice == "3":
        player.inventory.append(store[2].name)
        player.money -= store[2].price
        print(f'{store[2].name}을 구매했습니다.')

    elif player.money >= store[3].price and choice == "4":
        player.inventory.append(store[3].name)
        player.money -= store[3].price
        print(f'{store[3].name}을 구매했습니다.')
    else:
        print('골드가 부족합니다.')
