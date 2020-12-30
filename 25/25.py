testing = False

import shared

MOD = 20201227

# import text from file
if testing:
    text = shared.read_input("input_test")
    #text = shared.read_input("input")
    print(f"input: {text}")
else:
    text = shared.read_input("input")

def get_keys(text):
    if testing:
        print(f"card public key: {text[0]}")
        print(f"door public key: {text[1]}")
    return text[0], text[1]

def find_loopsize(pubkey):
    n = 1
    for loop_size in range(1, MOD):
        n = n * 7 % MOD
        if n == pubkey:
            return loop_size
    return

def transform(subject, loopsize):
    n = 1
    for _ in range(loopsize):
        n = (n * subject) % MOD
    return n

def find_encryptionkey(card_pubkey, door_pubkey):
    card_loopsize = find_loopsize(card_pubkey)
    #door_loopsize = find_loopsize(door_pubkey)
    if testing:
        print(f"card loop size: {card_loopsize}")
        #print(f"door loop size: {door_loopsize}")
    return transform(door_pubkey, card_loopsize)

# Day 25
card_pubkey, door_pubkey = get_keys(text)
encrpytion_key = find_encryptionkey(card_pubkey, door_pubkey)
print(f"[Encryption Key] {encrpytion_key}")

# Display the time this took to run
shared.printTimeElapsed()
