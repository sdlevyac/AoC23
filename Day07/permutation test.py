Hand = list("QJJQ2")

cards = ["2","3","4","5","6","7","8","9","T","J", "Q","K","A"]

def permute(hand, permutations = []):
    if "j" in hand:
        index = hand.index("j")
        for card in cards:
            handCopy = [c for c in hand]
            handCopy[index] = card
            print(handCopy)
            input()
            permutations.extend(permute(handCopy, [handCopy]))
            #permutations.extend()
    return permutations

Hand = [card if card != "J" else "j" for card in Hand]

p = permute(Hand)

for permutation in p:
    print(permutation)