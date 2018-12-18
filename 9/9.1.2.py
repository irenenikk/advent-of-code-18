class Marble:
    def __init__(self, number, left, right):
        self.number = number
        self.left = left
        self.right = right

    def __str__(self):
     return "left: " + str(self.left) + ", right: " + str(self.right) + ", no: " + str(self.number)

def is_special_number(n):
    return n % 23 == 0

def add_marble_normally(i, current_marble, marbles):
    # find the numbers of the neighbors of the new marble
    right_neighbor = marbles[marbles[current_marble].right].right
    left_neighbor = marbles[current_marble].right
    # change the references of the neighbors
    marbles[left_neighbor].right = i
    marbles[right_neighbor].left = i
    # create and add new marble with the neighbors
    marbles.append(Marble(i, left_neighbor, right_neighbor))
    return i

def change_player_turn(current_player, no_players):
    return (current_player + 1) % no_players

def remove_7th_marble(current_marble, marbles):
    next_iterable = -1
    # traverse to the seventh marble
    for i in range(7):
        next_iterable = marbles[next_iterable].left
    left_neighbor = marbles[next_iterable].left
    right_neighbor = marbles[next_iterable].right
    # remove references to removable marble
    marbles[left_neighbor].right = right_neighbor
    marbles[right_neighbor].left = left_neighbor
    return next_iterable,  right_neighbor


no_players = 441
last_marble = 71032 * 100

# initalize with the first marble
marbles = [Marble(0, 0, 0)]
current_marble = 0
current_player = 0
scores = [0] * no_players
for i in range(1, last_marble+1):
    if is_special_number(i):
        scores[current_player] += i
        score, current_marble = remove_7th_marble(current_marble, marbles)
        # add the marble to the marbles list without references
        # this qurantees that index corresponds to number of marble
        marbles.append(Marble(i, None, None))
        scores[current_player] += score
    else:
        current_marble = add_marble_normally(i, current_marble, marbles)
    current_player = change_player_turn(current_player, no_players)
print(max(scores))