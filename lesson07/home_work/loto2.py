import random

num_offered_base = [num for num in range(90)]

rows = 3
columns = 9

class Card:
    def __init__(self):
        self.data = [[' ' for _ in range(columns)] for _ in range(rows)]

        row_nums_base = [_ for _ in range(1, 91)]
        row_nums = [sorted(random.sample(row_nums_base, 5)) for _ in range(3)]
        row_indexes = [sorted(random.sample(range(columns), 5)) for _ in range(3)]
        for row in range(rows):
            for i, el in enumerate(self.data[row]):
                if i in row_indexes[row]:
                    self.data[row][i] = row_nums[row][0]
                    row_nums[row].remove(row_nums[row][0])

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

def debug():
    human_card = Card()
    computer_card = Card()
    human_card.print('Human')


debug()