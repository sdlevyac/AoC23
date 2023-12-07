filename = "inputSmall.txt"
filename = "inputBig.txt"

cardValues = {str(i):i for i in range(2,10)}
cardValues["T"] = 10
cardValues["J"] = 11
cardValues["Q"] = 12
cardValues["K"] = 13
cardValues["A"] = 14

def rank(hand):
    fullRank = [cardValues[c] for c in hand]
    return fullRank

data = open(filename).read().split("\n")
hands = [list(line.split(" ")[0]) for line in data]
bids = [int(line.split(" ")[1]) for line in data]
handRanks = [int("".join([f'{r:02d}' for r in rank(hand)])) for hand in hands]

def score(hand):
    dictHand = {}
    for card in hand:
        if card not in dictHand:
            dictHand[card] = 1
        else:
            dictHand[card] += 1
    if len(dictHand) == 1:
        #print("5 of a kind", end=":")
        return 7
    elif len(dictHand) == 2:
        for card in hand:
            if dictHand[card] == 4:
                #print("4 of a kind", end=":")
                return 6
            if dictHand[card] == 3:
                #print("full house", end=":")
                return 5
    elif len(dictHand) == 3:
        pairs = 0
        for card in hand:
            if dictHand[card] == 3:
                #print("3 of a kind", end=":")
                return 4
            if dictHand[card] == 2:
                pairs += 1
            if pairs == 2:
                #print("2 pairs", end=":")
                return 3
    elif len(dictHand) == 4:
        #print("1 pair", end=":")
        return 2
    elif len(dictHand) == 5:
        #print("high card", end=":")
        return 1

handScores = {}

for i, hand in enumerate(hands):
    handScores[i] = score(hand)

indices = list(range(len(hands)))
indices = [i for _,i in sorted(zip(handScores.values(), indices))][::-1]

scoreGroups = {}

for score in range(8):
    scoreGroups[score] = [index for index in indices if handScores[index] == score]

allbids = []

for score in scoreGroups:
    scoreGroup = scoreGroups[score]
    theseHands = [hands[index] for index in scoreGroup]
    theseHandRanks = [handRanks[index] for index in scoreGroup]
    theseIndices = [index for index in scoreGroup]
    theseBids = [bids[index] for index in scoreGroup]
    


    theseHands = [i for _,i in sorted(zip(theseHandRanks, theseHands))][::-1]
    theseIndices = [i for _,i in sorted(zip(theseHandRanks, theseIndices))][::-1]
    theseBids = [i for _,i in sorted(zip(theseHandRanks, theseBids))][::-1]



    allbids.extend(theseBids[::-1])

print(allbids)
vals = [bid * (i + 1) for i,bid in enumerate(allbids)]
print(sum(vals))