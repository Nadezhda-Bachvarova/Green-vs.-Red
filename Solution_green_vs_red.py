x, y = [int(x) for x in input().split(', ')]
generation_zero = []

if x <= y < 1000:
    for _ in range(y):
        generation_zero.append(input())

x1, y1, N = [int(x) for x in input().split(', ')]
look_for_cell = generation_zero[x1][y1]


def check_red_cell(kwargs):
    green_neighbors = list(kwargs).count(1)
    if green_neighbors in [3, 6]:
        return True
    elif green_neighbors not in [0, 1, 2, 4, 5, 7, 8]:
        return False


def check_green_cell(kwargs):
    green_neighbors = list(kwargs).count(1)
    if green_neighbors in [0, 1, 4, 5, 7, 8]:
        return True
    elif green_neighbors in [2, 3, 6]:
        return False


position = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1],
    'up_left': [-1, -1],
    'up_right': [-1, 1],
    'down_left': [1, -1],
    'down_right': [1, 1],
}


class Neighbors:
    green_counter = 0
    new_generation = [['' for _ in range(x)] for i in range(y)]
    for generation in range(1, N + 1):
        for row in range(y):
            for col in range(x):
                current_cell = generation_zero[row][col]
                neighbors = []
                if x1 == row and y1 == col and current_cell == '1':
                    green_counter += 1
                if col == 0:
                    if row == 0:
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        right_neighbor = generation_zero[position['right'][0] + row][position['right'][1] + col]
                        down_right_neighbor = generation_zero[position['down_right'][0] + row][position['down_right'][1] + col]
                        neighbors.extend(int(i) for i in [down_neighbor, right_neighbor, down_right_neighbor])
                    elif row < y - 1:
                        up_neighbor = generation_zero[position['up'][0] + row][position['up'][1] + col]
                        up_right_neighbor = generation_zero[position['up_right'][0] + row][position['up_right'][1] + col]
                        right_neighbor = generation_zero[position['right'][0] + row][position['right'][1] + col]
                        down_right_neighbor = generation_zero[position['down_right'][0] + row][position['down_right'][1] + col]
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        neighbors.extend(int(i) for i in [up_neighbor, up_right_neighbor, right_neighbor, down_right_neighbor, down_neighbor])
                    elif row == y - 1:
                        up_neighbor = generation_zero[position['up'][0] + row][position['up'][1] + col]
                        up_right_neighbor = generation_zero[position['up_right'][0] + row][position['up_right'][1] + col]
                        right_neighbor = generation_zero[position['right'][0] + row][position['right'][1] + col]
                        neighbors.extend(int(i) for i in [up_neighbor, up_right_neighbor, right_neighbor])
                elif 0 < col < x - 1:
                    if row == 0:
                        left_neighbor = generation_zero[position['left'][0] + row][position['left'][1] + col]
                        down_left_neighbor = generation_zero[position['down_left'][0] + row][position['down_left'][1] + col]
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        down_right_neighbor = generation_zero[position['down_right'][0] + row][position['down_right'][1] + col]
                        right_neighbor = generation_zero[position['right'][0] + row][position['right'][1] + col]
                        neighbors.extend(int(i) for i in [left_neighbor, down_left_neighbor, down_neighbor, down_right_neighbor, right_neighbor])
                    elif 0 < row < y - 1:
                        up_neighbor = generation_zero[position['up'][0] + row][position['up'][1] + col]
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        right_neighbor = generation_zero[position['right'][0] + row][position['right'][1] + col]
                        left_neighbor = generation_zero[position['left'][0] + row][position['left'][1] + col]
                        up_left_neighbor = generation_zero[position['up_left'][0] + row][position['up_left'][1] + col]
                        up_right_neighbor = generation_zero[position['up_right'][0] + row][position['up_right'][1] + col]
                        down_right_neighbor = generation_zero[position['down_right'][0] + row][position['down_right'][1] + col]
                        down_left_neighbor = generation_zero[position['down_left'][0] + row][position['down_left'][1] + col]
                        neighbors.extend(int(i) for i in [up_neighbor, down_neighbor, right_neighbor, left_neighbor, up_left_neighbor,
                                           up_right_neighbor, down_right_neighbor, down_left_neighbor])
                    elif row == y - 1:
                        up_neighbor = generation_zero [position ['up'] [0] + row] [position ['up'] [1] + col]
                        right_neighbor = generation_zero [position ['right'] [0] + row] [position ['right'] [1] + col]
                        left_neighbor = generation_zero [position ['left'] [0] + row] [position ['left'] [1] + col]
                        up_left_neighbor = generation_zero [position ['up_left'] [0] + row] [
                            position ['up_left'] [1] + col]
                        up_right_neighbor = generation_zero [position ['up_right'] [0] + row] [
                            position ['up_right'] [1] + col]
                        neighbors.extend (int (i) for i in
                                          [left_neighbor, up_left_neighbor, up_neighbor, up_right_neighbor,
                                           right_neighbor])
                elif col == x - 1:
                    if row == 0:
                        left_neighbor = generation_zero[position['left'][0] + row][position['left'][1] + col]
                        down_left_neighbor = generation_zero[position['down_left'][0] + row][position['down_left'][1] + col]
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        neighbors.extend(int(i) for i in [left_neighbor, down_left_neighbor, down_neighbor])
                    elif row == y - 1:
                        up_neighbor = generation_zero [position ['up'] [0] + row] [position ['up'] [1] + col]
                        up_left_neighbor = generation_zero [position ['up_left'] [0] + row] [
                            position ['up_left'] [1] + col]
                        left_neighbor = generation_zero [position ['left'] [0] + row] [position ['left'] [1] + col]
                        neighbors.extend (int (i) for i in [up_neighbor, up_left_neighbor, left_neighbor])
                    else:
                        up_neighbor = generation_zero[position['up'][0] + row][position['up'][1] + col]
                        up_left_neighbor = generation_zero[position['up_left'][0] + row][position['up_left'][1] + col]
                        left_neighbor = generation_zero[position['left'][0] + row][position['left'][1] + col]
                        down_left_neighbor = generation_zero[position['down_left'][0] + row][position['down_left'][1] + col]
                        down_neighbor = generation_zero[position['down'][0] + row][position['down'][1] + col]
                        neighbors.extend(int(i) for i in [up_neighbor, up_left_neighbor, left_neighbor, down_left_neighbor, down_neighbor])

                if int(current_cell) == 0:
                    if check_red_cell(neighbors):
                        new_generation[row][col] = '1'
                    else:
                        new_generation[row][col] = '0'
                else:
                    if check_green_cell(neighbors):
                        new_generation[row][col] = '0'
                    else:
                        new_generation[row][col] = '1'

        generation_zero = new_generation
        new_generation = [['' for _ in range(x)] for i in range(y)]
    print(green_counter)