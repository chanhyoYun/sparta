class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f'[{self.name}] 판매 가격은 [{self.price}]')

    def discard(self):
        if self.isdropable:
            print(f'[{self.name}] 아이템을 버렸습니다.')
        else:
            print(f'[{self.name}] 아이템을 버릴 수 없습니다.')


class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f'[{self.name}] 착용했습니다.{self.effect}')


class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f'[{self.name}] 사용했습니다.{self.effect}')


sword = WearableItem('강철검', 30000, 3.5, True, '체력 50 증가, 마력 3000 증가')
sword.wear()
sword.sale()
sword.discard()

print('⚔--------------------------------------------------------⚔')
print('⚔--------------------------------------------------------⚔')
armor = WearableItem('철갑옷', 50000, 3.5, True, 'HP 50 증가, 마력 9000 증가')
armor.wear()
armor.sale()
armor.discard()

print('⚚--------------------------------------------------------⚚')
print('⚚--------------------------------------------------------⚚')
potion = UsableItem('HP포션', 1500000, 0.1, False, '효과 300초 지속 전부회복')
potion.discard()
potion.sale()
potion.use()

print('⚚--------------------------------------------------------⚚')
print('⚚--------------------------------------------------------⚚')
potion2 = UsableItem('MP포션', 1500000, 0.1, False, '효과 300초 지속 전부회복')
potion2.discard()
potion2.sale()
potion2.use()
