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

def play_recursive_combat(player1, player2, game=1):
    if testing:
        print(f"\n=== Game {game} ===")
    round = 1
    sub_game = game
    cache = set()
    while player1.is_not_empty() and player2.is_not_empty():
        if testing:
            print(f"\n-- Round {round} (Game {game}) --")
            print(player1)
            print(player2)
        play = (tuple(player1.cards), tuple(player2.cards))
        if play in cache:
            winner = player1
            if testing:
                print(f"{winner.id} wins round {round} of game {game}!")
            return winner, game
        cache.add(play)
        A = player1.pop()
        B = player2.pop()
        if (A <= len(player1.cards)) and (B <= len(player2.cards)):
            if testing:
                print(f"Playing a sub-game to determine the winner...")
            sub_player1 = Deck(player1.id, player1.cards[:A])
            sub_player2 = Deck(player2.id, player2.cards[:B])
            winner, sub_game = play_recursive_combat(sub_player1, sub_player2, sub_game + 1)
        else:
            if A > B:
                winner = player1
            else:
                winner = player2
        if testing:
            print(f"{winner.id} wins round {round} of game {game}!")
        if winner.id == player1.id:
            player1.win(A, B)
        else:
            player2.win(B, A)
        round += 1
    if player1.is_not_empty():
        gamewinner = player1
    else:
        gamewinner = player2
    if testing:
        print(f"The winner of game {game} is {gamewinner.id}!")
    if testing and (game == 1):
        print(f"\n\n== Post-game results ==")
        print(player1)
        print(player2)
    elif testing and (game >= 2):
        print(f"\n...anyway, back to game {game - 1}.")
    return gamewinner, game

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(text)
else:
    text = shared.read_input("input")

# Part 2
player1, player2 = init_players(text)
winner, _ = play_recursive_combat(player1, player2)
part2 = calculate_score(winner)
print(f"[Part 2] {part2}")

# Display the time this took to run
shared.printTimeElapsed()
