from random import randint

#Dictionary of Ranks, with their associated order numbered out.
ranks = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}

#List of Suits
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

#Dictionary of Poker Hands with their associated hand ranking.
hands = {"High Card": 1, "Pair": 2, "Two Pairs": 3, "Three of a Kind": 4, "Straight": 5, "Flush": 6, "Full House": 7, "Four of a Kind": 8, "Straight Flush": 9, "Royal Flush": 10}

players = []

#The Card class object, containing a card's rank, suit and value. 
class Card(object):
  value = 0
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    self.value = ranks[rank]

class Player(object):
  wins = 0
  losses = 0
  wallet = 0
  name = ""
  
  def __init__(self, name, wallet):
    self.wallet = wallet
    self.name = name
    self.hand = []
    self.bet = 0

#Helper Functions

#Prints a card to the console
def printCard(card):
  print(card.rank + " of " + card.suit)

#Prints a list of cards to the console
def printDeck(deck):
    for c in deck:
        printCard(c)

#Deals one card from a deck / hand to a hand / deck
def deal(P, D):
    P.hand.append(D.pop(randint(0, len(D) - 1)))

#Sorts hand in ascending order, for straight purposes
def sortHand(hand):
    values = []
    sortedHand = []

    #Creates a integer list of the values of the cards
    for c in hand:
        values.append(c.value)

    for v in range(len(values)):
        #gets the index in values of the smallest element
        i = values.index(min(values))
        #appends the card at index i from hand to sortedHand
        sortedHand.append(hand[i])
        #Makes that smallest value into a very high value, so the next min(value) gets the next smallest value
        values[i] = 20
    return sortedHand 

#Checks a hand for an Ace and returns the index
def checkForAce(hand):
    for c in hand:
        if c.rank == "Ace":
            return hand.index(c)
    return False

#Checks a hand for a King and returns the index (for straight purposes)
def checkForKing(hand):
    for c in hand:
        if c.rank == "King":
            return hand.index(c)
    return False

#Alternative Pair Check, which should only return the pair if they are the only two cards of a given rank in the hand!
def checkForPair(hand):
    for i in range(len(hand)):
        total = 1
        r = hand[i].rank
        pair = [hand[i]]
        for j in range(len(hand)):
            if hand[i] != hand[j] and r == hand[j].rank:
                total += 1
                pair.append(hand[j])
        if total == 2:
            return pair
    return False
            

#Checks to see if a player's hand has a Pair
#DEPRECIATED!! 
"""def checkForPair(hand):
    for i in range(len(hand)):
        for j in range(i+1, len(hand)):
            if hand[i].rank == hand[j].rank:
                return hand[i], hand[j]
    return False"""

#Checks to see if a player's hand contains Two Pairs
def checkForTwoPairs(hand):
    if checkForPair(hand) != False:
        pair = [checkForPair(hand)[0], checkForPair(hand)[1]]
        checkForPair(hand)
        handNoPair = hand.copy()
        handNoPair.remove(pair[0])
        handNoPair.remove(pair[1])
        if checkForPair(handNoPair) != False:
            return checkForPair(handNoPair)
    return False

#Checks to see if a player's hand contains a Three of a Kind
def checkForThreeOfAKind(hand):
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                if hand[i].rank == hand[j].rank and hand[j].rank == hand[k].rank:
                    return hand[i], hand[j], hand[k]
    return False

#Checks to see if a player's hand contains a Four of a Kind
def checkForFourOfAKind(hand):
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                for l in range(k+1, len(hand)):
                    if hand[i].rank == hand[j].rank and hand[j].rank == hand[k].rank and hand[k].rank == hand[l].rank:
                        return hand[i], hand[j], hand[k], hand[l]
    return False

#Checks to see if a player's hand contains a Full House
def checkForFullHouse(hand):
    workingHand = []
    for c in hand:
        workingHand.append(c)
    if checkForPair(hand) != False:
        pair = [checkForPair(hand)[0], checkForPair(hand)[1]]
        workingHand.remove(pair[0])
        workingHand.remove(pair[1])
        if checkForThreeOfAKind(workingHand) != False:
            return checkForPair(hand), checkForThreeOfAKind(workingHand)
    return False



#Checks to see if a player's hand contains a Flush
def checkForFlush(hand):
    desiredSuit = hand[0].suit
    for c in hand:
        if c.suit != desiredSuit:
            break
    else:
        return hand
    return False

#Checks to see if a player's hand contains a Straight
def checkForStraight(hand):
    testingHand = []
    for c in hand:
        testingHand.append(c)

    if checkForAce(hand) != False and checkForKing(hand) != False:
        aceInteger = checkForAce(testingHand)
        testingHand[aceInteger].rank = 14
    
    testingHand = sortHand(testingHand)
    for i in range(len(testingHand) - 1):
        if testingHand[i].value != (testingHand[i + 1].value - 1):
            break
    else:
        return hand
    return False

#Checks to see if a player's hand contains a Straight Flush
def checkForStraightFlush(hand):
    if checkForStraight(hand) != False and checkForFlush(hand) != False:
        return hand
    return False

#Checks to see if a player's hand contains a Royal Flush
def checkForRoyalFlush(hand):
    royal = ["Ten", "Jack", "Queen", "King", "Ace"]
    handRanks = []
    for c in hand:
        handRanks.append(c.rank)
    if all(r in handRanks for r in royal) and checkForFlush(hand) != False:
        return hand
    return False

#Return whatever hand type this hand qualifies as, in string format.
def checkHand(hand):
    if checkForRoyalFlush(hand) != False:
        return "Royal Flush"
    elif checkForStraightFlush(hand) != False:
        return "Straight Flush"
    elif checkForFourOfAKind(hand) != False:
        return "Four of a Kind"
    elif checkForFullHouse(hand) != False:
        return "Full House"
    elif checkForFlush(hand) != False:
        return "Flush"
    elif checkForStraight(hand) != False:
        return "Straight"
    elif checkForThreeOfAKind(hand) != False:
        return "Three of a Kind"
    elif checkForTwoPairs(hand) != False:
        return "Two Pairs"
    elif checkForPair(hand) != False:
        return "Pair"
    else:
        return "High Card"

def createPlayer():
    name = input("Please Enter Your Name: ")
    chips = input("\nPlease Enter Your Chips (NOTE: Blinds Start at 25 Chips): ")
    player = Player(name, chips)
    players.append(player)

#Taking in a player and a starting ante (a), the player must choose to Call, Raise, or Fold. Calling sets their bet equal to the current ante, Raising increases their bet and the ante, and Folding leaves their bet as it was. This function returns the type of play the player made, along with the new ante
def bet(player, a):
    #The minimum required funds for a player to place a bet, the current ante minus their current bet
    requiredFunds = a - player.bet
    while True:
        if player.wallet <= requiredFunds:
            RCF = input("Would you like to Call or Fold? ")
        else:
            RCF = input("Would you like to Raise, Call, or Fold? ")
        
        if RCF == "Fold":
            return "Fold", 0
        
        elif RCF == "Call":
            if player.wallet <= requiredFunds:
                player.wallet = 0
            else:
                player.wallet -= a
                player.bet = a
            return "Call", a
        
        elif RCF == "Raise":
            while True:
                newAnte = input("How much would you like to Raise? ")
                if not newAnte.isdigit():
                    print("Please enter a non-decimal number!")
                else:
                    newAnte = int(newAnte)
                    if newAnte <= 0:
                        print("You must raise above zero!")
                    else:
                        player.wallet -= newAnte
                        player.bet = newAnte
                        return "Raise", newAnte
        else:
            print("Please Type Raise, Call, or Fold, for your answer.")


def roundOfBetting(pool):
    newPool = pool
    rollingAnte = ante
    for player in players:
            #For Each player, match or fold
            betAnte = bet(player, ante)
            ante = betAnte[1]
            #If the player raised, do another round of betting
            if betAnte[0] == "Raise":
    return newPool

def gameRound():
    #Deal five cards to each player, then print.
    pool = 0
    blind = 25
    for player in players:
        for i in range(5):
            deal(player, deck)
        printDeck(player.hand)
    
    #Give each player a chance to raise their bets before discard phase
    
        
                
    # 
    #

def game():
    numPlayers = input("How Many Players are at The Table? ")

    #Create numPlayers number of Players
    for i in numPlayers:
        createPlayer()

    roundNumber = 0

    #While there are still players still in the game...
    while len(players) > 0:
        gameRound()




# Game Running Code
pool = 0

house = Player("Mr. House", 5000000)





# Makes a Standard Deck of Cards
deck = []

for i in ranks:
    for j in suits:
        newCard = Card(i, j)


#Testing Zone

tc1 = Card("Five", "Diamonds")
tc2 = Card("Five", "Dogs")
tc3 = Card("Three", "Diamonds")
tc4 = Card("Two", "Diamonds")
tc5 = Card("Two", "Diamonds")

testPlayer = Player("Tester", 100)

testPlayer.hand.append(tc1)
testPlayer.hand.append(tc2)
testPlayer.hand.append(tc3)
testPlayer.hand.append(tc4)
testPlayer.hand.append(tc5)

for c in testPlayer.hand:
    printCard(c)
print("\n")

print(checkHand(testPlayer.hand))
