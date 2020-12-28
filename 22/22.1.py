testing = False

import shared

class Deck:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards
    
    def __str__(self):
        return f"{self.id}'s deck: {', '.join(map(str, self.cards))}"

    def pop(self):
        card = self.cards.pop(0)
        if testing:
            print(f"{self.id} plays: {card}")
        return card
    
    def win(self, A, B):
        if testing:
            print(f"{self.id} wins the round!")
        self.cards.append(A)
        self.cards.append(B)
        return

    def is_not_empty(self):
        if len(self.cards) == 0:
            return False
        else:
            return True

def init_players(text):
    if testing:
        print(f"-- Initializing players from input --")
    players = []
    for i, raw_player in enumerate(text):
        raw_id = raw_player.splitlines()[0].split(':')[0]
        raw_cards = list(map(int, raw_player.splitlines()[1:]))
        players.append(Deck(raw_id, raw_cards))
        if testing:
            print(f"{players[i].id} created with cards: {players[i].cards}")
    return (p for p in players)

def calculate_score(winner):
    score = 0
    for idx, card in enumerate(winner.cards):
        score += card * (len(winner.cards) - idx)
        if testing:
            print(f"{card} * {len(winner.cards) - idx}")
    if testing:
        print(f"score: {score}")
    return score

def play_game(player1, player2):
    n = 0
    while player1.is_not_empty() and player2.is_not_empty():
        if testing:
            print(f"-- Round {n} --")
            print(player1)
            print(player2)
        A = player1.pop()
        B = player2.pop()
        if A > B:
            player1.win(A, B)
        else:
            player2.win(B, A)
        if testing:
            print()
        n += 1
    if testing:
        print(f"\n== Post-game results ==")
        print(player1)
        print(player2)
    if player1.is_not_empty():
        winner = player1
    else:
        winner = player2
    return calculate_score(winner)

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(text)
else:
    text = shared.read_input("input")

# Part 1
player1, player2 = init_players(text)
part1 = play_game(player1, player2)
print(f"[Part 1] {part1}")

# Display the time this took to run
shared.printTimeElapsed()
