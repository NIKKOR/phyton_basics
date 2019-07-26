import random

num_offered_base = [num for num in range(1, 91)]

rows = 3
columns = 9

class Card:
    def __init__(self):
        self.data = [[' ' for _ in range(columns)] for _ in range(rows)]

        row_nums_base = [_ for _ in range(1, 91)]
        # self.row_nums = [sorted(random.sample(row_nums_base, 5)) for _ in range(3)]
        self.row_nums = [[' ' for _ in range(5)] for _ in range(rows)]
        for i in range(rows):
            for y in range(5):
                self.row_nums[i][y] = random.choice(row_nums_base)
                row_nums_base.remove(self.row_nums[i][y])
            self.row_nums[i] = sorted(self.row_nums[i])
        row_indexes = [sorted(random.sample(range(columns), 5)) for _ in range(3)]
        for row in range(rows):
            for i, el in enumerate(self.data[row]):
                if i in row_indexes[row]:
                    self.data[row][i] = self.row_nums[row][0]
                    self.row_nums[row].remove(self.row_nums[row][0])

    def data_print(self, data_row):
        self.data_row = data_row
        self.data_row_str = ''
        for el in self.data_row:
            self.data_row_str += str(el) + ' '
        return self.data_row_str

    def print(self, property):
        print('{0:.^25}\n{1:^25}\n'
              '{2:^25}\n{3:^25}\n'
              '{4:.^25}'.format(
            'Ваша карточка' if property == 'Human' else 'Карточка компьютера',
            f'{self.data_print(self.data[0])}',
            f'{self.data_print(self.data[1])}',
            f'{self.data_print(self.data[2])}', ''))

def print_num_offered(base_def):
    base = base_def
    ran_num = random.choice(base)
    base.remove(ran_num)
    print(f'\nНовый бочонок: {ran_num if not debug_mode else computer_card.data[0][0]} (осталось {len(base)})')
    return [base, ran_num if not debug_mode else computer_card.row_nums[1] ]

def endgame(player):
    return True, f'{player} проиграл. Победитель - {"Человек" if player == "Компьютер" else "Компьютер"}'

def endgame_full(player):
    return endgame(player)[0], endgame(player)[1]

human_card = Card()
computer_card = Card()
quit_check = False
human_count = 0
computer_count = 0
queue = 0
debug_mode = True
while quit_check == False:
    if queue == 0:
        num_offered_full = print_num_offered(num_offered_base)
        num_offered_base = num_offered_full[0]
        num_offered = num_offered_full[1]
        human_card.print('Human')
        computer_card.print('Computer')
        choice = input('Зачеркнуть цифру (y/n)\n')

        if choice == 'y':
            win_check = False
            for row in range(rows):
                if num_offered in human_card.data[row]:
                    human_card.data[row][human_card.data[row].index(num_offered)] ='X'
                    human_count += 1
                    win_check = True
            for row in range(rows):
                if num_offered not in human_card.data[row] and win_check != True:
                    print(endgame_full('Человек')[1])
                    quit_check = endgame_full('Человек')[0]
        else:
            for row in range(rows):
                if num_offered in human_card.data[row]:
                    print(endgame_full('Человек')[1])
                    quit_check = endgame_full('Человек')[0]
        queue = 1
        continue

    else:
        # Очередь компьюетра
        num_offered_full = print_num_offered(num_offered_base)
        num_offered_base = num_offered_full[0]
        num_offered = num_offered_full[1]
        computer_card.print('Computer')
        human_card.print('Human')
        print('Зачеркнуть цифру (y/n)\n')
        choice = 'n'
        for row in range(rows):
            if num_offered in computer_card.data[row]:
                choice = 'y'

        print(f'Выбор компьютера: {choice}')
        if choice == 'y':
            win_check = False
            for row in range(rows):
                if num_offered in computer_card.data[row]:
                    computer_card.data[row][computer_card.data[row].index(num_offered)] = \
                    'X'
                    computer_count += 1
                    win_check = True
                if num_offered not in computer_card.data[row] and win_check != True:
                    print(endgame_full('Компьютер')[1])
                    quit_check = endgame_full('Компьютер')[0]
        else:
            for row in range(rows):
                if num_offered in computer_card.data[row]:
                    print(endgame_full('Компьютер')[1])
                    quit_check = endgame_full('Компьютер')[0]

    queue = 0

    if computer_count == 15:
        endgame_full('Человек')
        quit_check = endgame_full('Человек')
    elif human_count == 15:
        endgame_full('Компьютер')
        quit_check = endgame_full('Компьютер')
        """
        Я раблотал над дебажным модом. Хотел сделать так, 
        чтобы при новой игре новым бочнком тановился первый элемент карточки компьютера.
        """