class Animal:
    def __init__(self, type):
        self.name = input('введите имя питомца:')
        self.type = type
        self.age = 0.1
        self.sex = input('введите пол питомца:')
        self.weight = 1
        self.time = 0

    def name(self):
        self.info()

    def sex(self):
        self.info()

    def menu(self):
        print('''выберите действие:
        1.выгулять
        2.покормить
        3.уложить спать''')
        a = int(input('введите цифру:'))

        if a == 1:
            self.walk()
        elif a == 2:
            self.eat()
        elif a == 3:
            self.dream()

    def walk(self):
        print('''погулять с питомцем?:
        1.да
        2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('ваш питомец на прогулке')
            self.age += 0.1
            self.weight += 0.1
            self.info()
        elif a == 2:
            print('ваш питомец растроен')
            self.age -= 0.1
            self.weight -= 0.1
            self.info()

    def eat(self):
        print('''ваш питомец хочет кушать:
        покормить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('''выберите чем покормить:
            1.мясо,рыба,паштет,кости,молоко
            2.яблоко,конфеты,виноград,суп''')
            b = input('введите название еды:')
            if b == 'мясо' or 'рыба' or 'кости' or 'паштет' or 'молоко':
                self.weight += 0.2
                self.age += 0.2
                self.info()
            elif b == 'яблоко' or 'конфеты' or 'виноград' or 'суп':
                self.weight -= 0.2
                self.age -= 0.2
                self.info()
        elif a == 2:
            print('ваш питомец хочет кушать')
            self.weight -= 0.3
            self.age -= 0.3
            self.info()

    def dream(self):
        print('''ваш питомец хочет спать:
        уложить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            self.weight += 0.2
            self.age += 0.2
            self.info
        elif a == 2:
            self.weight -= 0.2
            self.age -= 0.2
            self.info()

    def info(self):
        print(f'имя:{self.name}')
        print(f'пол:{self.sex}')
        print(f'возраст:{self.age}')
        print(f'вес:{self.weight}')


while True:
    animal1 = Animal(type='')
    while True:
        animal1.info()
        animal1.menu()


