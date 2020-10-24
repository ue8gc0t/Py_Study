from random import randint


class Card:
    def __init__(self):
        num_list = []
        while len(num_list) < 15:
            num = randint(1, 90)
            if num not in num_list:
                num_list.append(num)
        self.__card = [[num_list[i + j*5] for i in range(0, 5)] for j in range(0, 3)]
        for i in range(0, len(self.__card)):
            self.__card[i] = sorted(self.__card[i])
            for j in range(0, 4):
                self.__card[i].insert(randint(0, 5 + j), 0)

    def __str__(self):
        string = '#' * 26 + '\n'
        for row in self.__card:
            for el in row:
                if el == 0:
                    string += '   '
                elif el < 10:
                    string += ' ' + str(el) + ' '
                elif el == 128:
                    string += ' - '
                else:
                    string += str(el) + ' '
            string += '\n'
        string += '#' * 26
        return string

    @property
    def get_card(self):
        return self.__card


class Session:
    def game(self, human_card, comp_card):
        print("Начало игры")
        while True:
            num = next(Session.num_gen())
            print('\n' * 10)
            print(f'Число: {num}')
            print('Карта компьютера')
            print(comp_card)
            print('Ваша карта')
            print(human_card)
            answer = (lambda x: True if x == 'Y' else False)(input('Зачеркнуть Y/N?: '))
            self.comp_answer(comp_card.get_card, num)
            if self.chek_answer(human_card.get_card, num) == answer:
                print('Продолжаем')
            else:
                print("Вы проиграли")
                break

    def chek_answer(self, card, num):
        result = False
        for i in range(0, len(card)):
            for j in range(0, len(card[i])):
                if card[i][j] == num:
                    card[i][j] = 128
                    result = True
        return result

    def comp_answer(self, card, num):
        if randint(1, 101) < 98:
            return self.chek_answer(card, num)
        else:
            return not self.chek_answer(card, num)

    @staticmethod
    def num_gen():
        num_list = list(range(1, 91))
        while len(num_list) > 0:
            yield num_list.pop(randint(0, len(num_list) - 1))


human_card = Card()
comp_card = Card()
session = Session()
session.game(human_card, comp_card)

