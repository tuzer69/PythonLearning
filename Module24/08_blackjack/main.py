import random
from Deck import Deck


class Player:
    def __init__(self):
        self.score = 0

    def get_card(self, deck, num):
        self.score += deck.cards[num].value
        return deck.cards.pop(num).symbol


deck = Deck()
computer_score = 0
r = random.randint(1, len(deck.cards) - 1)
computer_score += deck.cards.pop(r).value
r = random.randint(1, len(deck.cards) - 1)
computer_score += deck.cards.pop(r).value

player = Player()
r = random.randint(1, len(deck.cards) - 1)
print( '-' * 20, '\n', 'Ваша рука: ', sep='', end='')
print(player.get_card(deck, r), end='')
r = random.randint(1, len(deck.cards) - 1)
print(player.get_card(deck, r))

while player.score < 21:
    r = random.randint(1, len(deck.cards) - 1)
    print('\t1. Взять карту', '\n', '\t2. Остановиться', sep='')
    action = int(input())
    if action == 1:
        print('-' * 20, '\n', 'Ваша рука: ', sep='', end='')
        print(player.get_card(deck, r))
    else: break

if player.score > 21:
    print('Вы проиграли, вас счет', player.score)
elif computer_score > player.score:
    print('Компьютер победил!, счет:', computer_score)
else:
    print('Поздравляю!. Вы выйграли', '\n', 'СЧЕТ компьютера: ',
          computer_score, '\n', 'ВАШ счет: ', player.score, sep='')
