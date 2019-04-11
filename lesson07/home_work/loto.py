#!/usr/bin/python3



# 1 stage: module import and main functions
from numpy import random
import copy
def generate_boch():
    boch_list = list(range(91))[1:]
    random.shuffle(boch_list)
    return boch_list

# 2. player classes

class Player:
    def __init__(self,name):
        self.name = name
        self.res = 0
        self.total = 0
        
    def generate_card(self):
        _boch_list = list(range(91))[1:]
        _card_row = random.choice(_boch_list,15)
        _card_row = [sorted(list(_card_row[i*5:i*5+5])) for i in range(3)]
        self.final_card = []
        for i in range(3):
            _a = list(range(9))
            random.shuffle(_a)
            _a = sorted(_a[:5])
            _row_list = list(" "*9)
            for j in range(len(_card_row[i])):
                _row_list[_a[j]] = _card_row[i][j]
            self.final_card.append(_row_list)
        #print(self.final_card)
        return self.final_card

    def show_card(self):
        _bord = int((24 - len(str(self.name)))/2)
        print('='*_bord+str(self.name)+'='*_bord)
        for i in self.final_card:
            self.row_str = ''
            for j in i:
                self.row_str += str(j)+' '
            print(self.row_str)
        
    def update_card(self, number):
        self.res = 0
        for i in self.final_card:
            for idx in range(len(i)):
                if i[idx] == number:
                    #print('Got it', number)
                    i[idx] = '-'
                    self.res = 1
                    self.total += 1
        return self.final_card


                

'''
player1 = Player('Nuran')
player1.generate_card()
player1.show_card()

player1.update_card(1)
player1.show_card()
'''
# 3. Основной код
game_round = generate_boch()
k = len(game_round)

player1_name = input('введите имя игрока: ')
player2_name = 'PC'
player1_name_oncard = 'Ваша карточка'
player2_name_oncard = 'Карточка компьютера'
# инициализация игроков и их карточек
player1 = Player(player1_name_oncard)
player2 = Player(player2_name_oncard)
player1.generate_card()
player2.generate_card()
player1_score = 0
player2_score = 0



while player1.total < 15 or player1.total < 15:
    print('START!!!')

    if k == 0:
        print('конец игры')
        if player1_score > player2_score:
            print(player1_name,'выиграл!')
        elif player1_score > player2_score:
            print(player2_name,'выиграл!')
        else:
            print('DRAW!!')
        print('итоговый счет: ', player1_score, ':', player2_score)
        break
    else:    

        for i in game_round:
            print('текущий счет: ', player1_score, ':', player2_score)
            message = 'новый бочонок '+str(i)+', осталось '+str(k-1)
            print(message)
            player1.show_card()
            player2.show_card()
            player1_answer = input('Зачеркнуть цифру? (y/n): ')
            #player1_card_before = copy.deepcopy(player1.final_card)
            if player1_answer == 'y' or player1_answer == 'Y':
                player1.update_card(i)
                if player1.res == 0:
                    print(player1_name, 'проиграл :(')
                    #break
                else:
                    print('угадал!')
                    player1_score += 1
            else:
                #player1.keep_card(i)
                player1.update_card(i)
                if player1.res == 0:
                    print(player1_name, 'продолжаем...')
                    player1_score += 1
                else:
                    print(player1_name, 'проиграл')
                    #break
            print('ход компьютера!')
            player2.update_card(i)
            if player2.res == 0:
                print(player2_name, 'проиграл :)')
            else:
                player2_score += 1
                #break
            k -= 1
    if player1_score > player2_score:
        print(player1_name,'выиграл!')
    elif player1_score > player2_score:
        print(player2_name,'выиграл!')
    else:
        print('DRAW!!')
    print('итоговый счет: ', player1_score, ':', player2_score)

       





"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""





















