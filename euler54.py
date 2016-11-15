from enum import Enum

#Sloppy main method. A few points of redundancy. Could make arrays and handle
#arbitrary number of players. Bored of this one though.

class HAND_RANK(Enum):
    HIGH = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE= 6
    FOUR = 7
    STRAIGHT_FLUSH=8
    ROYAL_FLUSH=9

def cardsToNums(cards):
    nums=[]
    for card in cards:
        if card[0] < 'A':
            nums.append(int(card[0]))
        elif card[0] == 'T':
            nums.append(10)
        elif card[0] == 'J':
            nums.append(11)
        elif card[0] == 'Q':
            nums.append(12)
        elif card[0] == 'K':
            nums.append(13)
        elif card[0] == 'A':
            nums.append(14)
        else:
            print "Invalid card:",card

    return nums

def allSameSuit(cards):

    suit=cards[0][len(cards[0])-1]
    for i in range(1,len(cards)):
        if cards[i][len(cards[i])-1] <> suit:
            return False

    return True

def getRank(nums,pairValue,nonPairValues):
    currentRank=HAND_RANK.HIGH
    pairStreak=0
    straightStreak=0
    for i in range(len(nums)-1):
        sameAsNext=(nums[i]==nums[i+1])
        if sameAsNext:
            pairStreak+=1
        else:
            if pairStreak == 0:
                nonPairValues.append(nums[i])
            if i == len(nums)-2:
                nonPairValues.append(nums[len(nums)-1])
        if ((not sameAsNext) or i==len(nums)-2) and pairStreak<>0:
            if pairStreak == 3:
                pairValue[0]+=1000000*nums[i]
                currentRank=HAND_RANK.FOUR
            elif pairStreak == 2:
                pairValue[0]+=10000*nums[i]
                if currentRank == HAND_RANK.ONE_PAIR:
                    currentRank=HAND_RANK.FULL_HOUSE
                else:
                    currentRank = HAND_RANK.THREE
            else:
                pairValue[0]+=100*nums[i]
                if currentRank == HAND_RANK.THREE:
                    currentRank=HAND_RANK.FULL_HOUSE
                elif currentRank == HAND_RANK.ONE_PAIR:
                    currentRank=HAND_RANK.TWO_PAIR
                else:
                    currentRank=HAND_RANK.ONE_PAIR
            pairStreak=0
        if (nums[i]==(nums[i+1]-1)):
            straightStreak+=1

    if straightStreak==4:
        return HAND_RANK.STRAIGHT

    return currentRank

playerOneWins=0
cardsInAHand=5
startWins=0
handsFile = open("poker.txt")

for line in handsFile:
    startWins=playerOneWins
    hands=line.rstrip().split(" ")
    handNumsOne=cardsToNums(hands[0:cardsInAHand])
    handNumsOne.sort()
    allSameSuitOne=allSameSuit(hands[0:cardsInAHand])
    handOnePairValue=[0]
    handOneNonPairValues=[]
    handRankOne=getRank(handNumsOne,handOnePairValue,handOneNonPairValues)
    handNumsTwo=cardsToNums(hands[cardsInAHand:])
    handNumsTwo.sort()
    allSameSuitTwo=allSameSuit(hands[cardsInAHand:])
    handTwoPairValue=[0]
    handTwoNonPairValues=[]
    handRankTwo=getRank(handNumsTwo,handTwoPairValue,handTwoNonPairValues)

    if handRankOne==HAND_RANK.STRAIGHT and allSameSuitOne:
        if handNumsOne[0] == 10:
            handRankOne=HAND_RANK.ROYAL_FLUSH
        else:
            handRankOne=HAND_RANK.STRAIGHT_FLUSH

    if handRankTwo==HAND_RANK.STRAIGHT and allSameSuitTwo:
        if handNumsTwo[0] == 10:
            handRankTwo=HAND_RANK.ROYAL_FLUSH
        else:
            handRankTwo=HAND_RANK.STRAIGHT_FLUSH    

    if handRankOne.value > handRankTwo.value:
        playerOneWins+=1
    elif handRankOne.value == handRankTwo.value:
        if handRankOne == HAND_RANK.STRAIGHT_FLUSH or handRankOne == HAND_RANK.STRAIGHT:
            if handNumsOne[0] > handNumsTwo[0]:
                playerOneWins+=1
        elif handRankOne == HAND_RANK.FLUSH or handRankOne == HAND_RANK.HIGH:
            for i in range(len(handNumsOne)-1,-1,-1):
                if handNumsOne[i] > handNumsTwo[i]:
                    playerOneWins+=1
                    break
                elif handNumsOne[i] < handNumsTwo[i]:
                    break
        elif handOnePairValue[0] > handTwoPairValue[0]:
            playerOneWins+=1
        elif handOnePairValue[0] == handTwoPairValue[0]:
            for i in range(len(handOneNonPairValues)-1,-1,-1):
                if handOneNonPairValues[i] > handTwoNonPairValues[i]:
                    playerOneWins+=1
                    break
                elif handOneNonPairValues[i] < handTwoNonPairValues[i]:
                    break

print "Result:",playerOneWins

