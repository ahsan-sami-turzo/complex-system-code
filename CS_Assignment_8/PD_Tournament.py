from random import randint

random_move = lambda: randint(0, 1)


# r = round (from 0 to 9 (10 rounds))
# my_history = all my moves in previous rounds
# op_history = all opponent's moves in previous rounds
# op_history[r - 1] = last opponent's move (in previous round)
# my_score = my current score
# op_score = opponent's current score

# write your strategy here
# the beginning of your strategy
def MyStrategy(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1
    if r == 9:
        return 0
    return op_history[r - 1]


# the end of your strategy


def Altruist(r, my_history, op_history, my_score, op_score):
    return 1


def Egoist(r, my_history, op_history, my_score, op_score):
    return 0


def TitForTat(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1
    return op_history[r - 1]


def Grudger(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1
    return min(op_history)


def Detective(r, my_history, op_history, my_score, op_score):
    if r == 0 or r == 2 or r == 3:
        return 1
    if r == 1:
        return 0
    if op_history[0:4] == [1, 1, 0, 1]:
        return op_history[r - 1]
    return 0


def Random(r, my_history, op_history, my_score, op_score):
    return random_move()


def Judas(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1  # cooperate in the first round
    if my_score >= op_score:
        return 1  # cooperate if we are winning
    else:
        return 0  # defect if we are losing


def Shylok(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1  # cooperate in the first round
    if my_score >= op_score:
        return 0  # defect if winning
    else:
        return 1  # cooperate if losing


def Santa(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1  # cooperate in the first round
    ci = my_history.count(1)  # number of times in a row I have cooperated
    di = my_history.count(0)  # number of times in a row I have defected
    C = sum(my_history)  # total number of my cooperation
    N = len(my_history)  # total number of rounds
    if N > 0:
        magic_number = ci * (C / N)
    else:
        magic_number = 10
    if N % 25 == 0:  # if it's the 25th or it's multiple round
        return 1  # cooperate
    elif N % 25 < magic_number:
        if N % 2 == 0:
            return 0  # defect
        else:
            return 1  # cooperate
    else:
        return op_history[r - 1]  # tit for tat


# Sherlock strategy
def Sherlock(r, my_history, op_history, my_score, op_score):
    if r < 2:
        return 1  # cooperate in the first two rounds
    else:
        # Calculate the frequency of cooperation of the opponent
        freq_coop = op_history.count(1) / len(op_history)

        # If the opponent cooperates more than 50% of the time, assume they are cooperative and reciprocate
        if freq_coop > 0.5:
            return 1
        else:
            # If the opponent has defected in the last three rounds, assume they are defecting and defect
            if op_history[-3:] == [0, 0, 0]:
                return 0
            else:
                # Otherwise, play tit for tat
                return op_history[r - 1]

# MyStrategy
given_strategies = [Altruist, Egoist, TitForTat, Grudger, Detective, Random]
turzo_strategies = [Judas, Santa, Sherlock]

strategies = [j for i in [given_strategies, turzo_strategies] for j in i]

matrix = {"00": (0, 0), "01": (5, -1), "10": (-1, 5), "11": (3, 3)}
rounds = 10

amount = len(strategies)
table = [[0] * amount for i in range(amount)]
results = [0] * amount


def game(p1, p2):
    s1 = 0
    s2 = 0
    om1 = []
    om2 = []
    for r in range(rounds):
        m1 = p1(r, om1, om2, s1, s2)
        m2 = p2(r, om2, om1, s2, s1)
        om1.append(m1)
        om2.append(m2)
        (ss1, ss2) = matrix[str(m1) + str(m2)]
        s1 += ss1
        s2 += ss2
    return (s1, s2)


for i in range(amount):
    for j in range(i, amount):
        (table[i][j], table[j][i]) = game(strategies[i], strategies[j])
    results[i] = sum(table[i]) - table[i][i]

placei = sorted(range(amount), key=lambda i: results[i], reverse=True)
place = sorted(range(1, amount + 1), key=lambda i: placei[i - 1])

strategies = [elem.__name__ for elem in strategies]
strlen = max(list(map(len, strategies)))
strategies2 = [(strlen - len(elem)) * ' ' + elem for elem in strategies]
strategies.append('Result')

for i in range(amount):
    table[i].append(results[i])

for i in range(amount):
    for j in range(amount + 1):
        table[i][j] = str(table[i][j])
        if len(table[i][j]) < len(strategies[j]):
            table[i][j] = (len(strategies[j]) - len(table[i][j])) * ' ' + table[i][j]

print('\n' + strlen * ' ' + '  '.join(strategies))
for i in range(amount):
    print(strategies2[i] + '  '.join(table[i]) + '   ' + str(place[i]))

print('\n' + '  ' * strlen * 2 + 'Winner: ' + strategies[placei[0]])
