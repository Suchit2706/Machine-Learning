import itertools
import time
import neural_network as nn
import random
import test
from matplotlib import pyplot as plt
# import filehandling2 as fl
from os import system, name
from colorama import Fore, Back, Style, init
init()


def get_count(arr):
    count = 0
    for l in range(len(arr)):
        if arr[l] == 0:
            count += 1
    return count


def calculate(inlayer3, weights1, bias1, weights2, bias2, error1, goku, q):
    hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
    hlayer1 = nn.cal_hid(inlayer3, weights1, hlayer1, bias1)
    y = nn.cal_out(hlayer1, weights2, bias2)
    error = nn.cal_error(y, t)
    if error1 > error:
        goku = q
        error1 = error
    return error1, goku


def game_board(inlayer, game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            # print("This position is occupied ")
            return game_map, False, inlayer
        # print("   " + "  ".join((Fore.LIGHTGREEN_EX + str(i)) for i in range(len(game_map))), Style.RESET_ALL)
        if not just_display:
            game_map[row][column] = player
        inlayer1 = []
        for i in range(0, 3):
            for j in range(0, 3):
                inlayer1.append(game_map[i][j])
        inlayer = inlayer1
        # for count, row in list(enumerate(game, start=0)):
            # print(Fore.LIGHTGREEN_EX + str(count), Fore.LIGHTRED_EX + str(row), Style.RESET_ALL)
        return game_map, True, inlayer
    except IndexError as e:
        # print("Error with arguments passed:", e)
        return game_map, False, inlayer
    except Exception as e:
        # print("Error:", e)
        return game_map, False, inlayer


def win(game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal_check
    for row in game:
        if all_same(row):
            # print(f"Winner!! \nPlayer {row[0]} won horizontally(-)")
            return True
    # Vertical_check
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            # print(f"Winner!!! \nPlayer {check[0]} won vertically(|)")
            return True

    # Diagonal_check(\)
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        # print(f"Winner! \nPlayer {diags[0]} won diagonally(\\)")
        return True

    # Diagonal_check(/)
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        # print(f"Winner!! \nPlayer {diags[0]} won diagonally(/)")
        return True

    fill = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if game[i][j] == 0:
                fill += 1
    if fill == 0:
        # print("Draw")
        return True
    return False


def clear():
    _ = system('cls')


inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
olayer = 0.0
weights1 = []   # input to hidden
weights2 = []   # hidden to output
bias1 = []
bias2 = 0.0
y = 0.0
t = 1.0
error = 0.0
p1count = 0
p2count = 0
epoch = 0
'''
weights1 = nn.w1(weights1)
bias1, bias2 = nn.bias(bias1, bias2)
weights2 = nn.w2(weights2)
epoch = 0'''
# weights1, weights2, bias1, bias2 = test.w()
acc0 = 0.8
errors = []
k = 0
play = True
player_choice = itertools.cycle([1, -1])
while play:
    # f = open('Data.txt', 'a')
    f2 = open('buffer.txt', 'a')
    t = 1
    move = 1
    game = [[0 for i in range(3)] for j in range(3)]
    game_won = False
    game, _, inlayer = game_board(inlayer, game, just_display=True)
    while not game_won:
        current_player = next(player_choice)
        # print(f"Current Player: {current_player}")
        played = False
        while not played:
            if current_player == -1:
                column_choice = random.randint(0, 2)
                row_choice = random.randint(0, 2)
            else:
                error1 = 2000
                goku = 0
                justplayed = 0
                for q in range(0, 9):
                    if inlayer[q] == 0:
                        inlayer2 = inlayer[:]
                        inlayer2[q] = 1
                        if move == 1:
                            weights1, weights2, bias1, bias2 = test.w1()
                        elif move == 2:
                            weights1, weights2, bias1, bias2 = test.w2()
                        elif move == 3:
                            weights1, weights2, bias1, bias2 = test.w3()
                        else:
                            weights1, weights2, bias1, bias2 = test.w()
                        error1, goku = calculate(inlayer2, weights1, bias1, weights2, bias2, error1, goku, q)
                move += 1
                if goku <= 2:
                    row_choice = 0
                    column_choice = goku
                elif goku <= 5:
                    row_choice = 1
                    column_choice = goku - 3
                else:
                    row_choice = 2
                    column_choice = goku % 3

                '''inlayer1 = inlayer
                inlayer1[goku] = 1
                s1 = str(inlayer1)
                s = str()
                for i in range(1, len(s1) - 1):
                    if s1[i] != ' ':
                        s += s1[i]
                s += '\n'
                f2.write(s)
                '''
            game, played, inlayer = game_board(inlayer, game, current_player, row_choice, column_choice)

        if win(game):
            t = 1
            if current_player == -1:
                t = 0
                p2count += 1
            else:
                p1count += 1
            game_won = True
            '''
            if move > 1:
                f2.close()
                f1 = open('buffer.txt', 'r')
                f1.seek(0, 0)
                f = open('move1.txt', 'a')
                count1 = f1.readline()
                s = str()
                for i in range(0, len(count1) - 1):
                    s += count1[i]
                s += ','
                s += str(t)
                s += '\n'
                f.write(s)
                f.close()
                f = open('move2.txt', 'a')
                count1 = f1.readline()
                s = str()
                for i in range(0, len(count1) - 1):
                    s += count1[i]
                s += ','
                s += str(t)
                s += '\n'
                f.write(s)
                f.close()
                if move > 3:
                    f = open('move3.txt', 'a')
                    count1 = f1.readline()
                    s = str()
                    for i in range(0, len(count1) - 1):
                        s += count1[i]
                    s += ','
                    s += str(t)
                    s += '\n'
                    f.write(s)
                    f.close()
                    for j in range(move - 4):
                        f = open('move4.txt', 'a')
                        count1 = f1.readline()
                        s = str()
                        for i in range(len(count1) - 1):
                            s += count1[i]
                        s += ','
                        s += str(t)
                        s += '\n'
                        f.write(s)
                        f.close()
                f1.close()
                f2.close()
            f2 = open('buffer.txt', 'w')
            f2.write('')
            f2.close()
            '''
            k = k + 1
            # errors.append(error)
            if k == 100000:
                '''
                if epoch <= 32:
                    play = True
                    acc = p1count / (p1count + p2count)
                    weights1, weights2, bias1, bias2 = fl.nn(weights1, weights2, bias1, bias2, acc, acc0)
                    acc0 = acc
                    f1 = open('Data.txt', 'w')
                    f1.write('')
                    f1.close()
                    print('Accuracy: ', acc)
                    print('Epoch: ', epoch)
                    epoch += 1
                    k = 0
                    p1count = 0
                    p2count = 0
                else:'''
                play = False
            else:
                # print("Sequence \n", k, ": ", error)
                # print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
                if k % 1000 == 0:
                    print(k)
                play = True
            '''again = input("________GAME OVER________ \n\nWould you like to play again? (y/n): ")
            if again.lower() == 'y':
                print("\n...Restarting...")
                time.sleep(2)
            elif again.lower() == 'n':
                print("well, bye")
                play = False
            else:
                print("wrong choice, idiot")
                play = False
            '''
# print("Sequence \n", k, ": ", error)
# print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
print(p1count, p2count)
# plt.plot(errors)
# plt.show()
