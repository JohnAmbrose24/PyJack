import random
#Lists of Ranks
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

#List of Suits
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

#The Card class object, containing a card's rank, suit and value. 
class Card(object):
  value = 0
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    if rank == "Two":
      self.value = 2
    if rank == "Three":
      self.value = 3
    if rank == "Four":
      self.value = 4
    if rank == "Five":
      self.value = 5
    if rank == "Six":
      self.value = 6
    if rank == "Seven":
      self.value = 7
    if rank == "Eight":
      self.value = 8
    if rank == "Nine":
      self.value = 9
    if rank == "Ten" or rank == "Jack" or rank == "Queen" or rank == "King":
      self.value = 10
    if rank == "Ace":
      self.value = 11
  
  def setValue(self, newValue):
    self.value = newValue

#The Player class object, containing a player's wallet and current bet 
class Player(object):
  wins = 0
  losses = 0
  bet = 0
  hand = []
  wallet = 0
  name = ""
  def __init__(self, name, wallet):
    self.wallet = wallet
    self.name = name


#Pops a card from the deck and adds it to the player's hand
def deal(deck, player):
  
  player.hand.append(deck.pop(random.randint(0, (len(deck) - 1))))

#Prints a specific card's rank and suit
def printCard(card):
  print(card.rank + " of " + card.suit)

#Prints a hand using the printCard function
def printHand(player):
  hand = player.hand
  print(player.name + "'s Hand:")
  for card in hand:
    printCard(card)
      
#Calculates the total value of a given list of cards
def handValue(hand):
  total = 0
  for card in hand:
    total += card.value
  return total 

def checkValue(hand):
  value = handValue(hand)
  if value > 21:
    print("OVER TWENTY-ONE! FIND AN ACE!!")
    fixAce(hand)
  else:
    return "Safe!"
  if value > 21:
    return "Bust!"

#Checks a hand for Aces that are being read as 11s, and changes them one-by-one until the hand is below 21.
def fixAce(hand):
  print("Trying to find an ace...")
  for i in range(len(hand)):
    #If the card is Ace and the value is 11...
    if hand[i].rank == "Ace" and hand[i].value == 11:
      print("FOUND ONE!!")
      hand[i].value = 1
      break
    else:
      #print("That wasn't an Ace!")
      pass

#Prints out Player stats
def playerStats(player):
  print("Player Name: ", player.name)
  print("Chips: ", player.wallet)
  print("Win/Loss Ratio:", player.wins, "/", player.losses)


#GAME RUNNING CODE

#Make the deck and player
deck = []
playerHand = []

#Fill the deck with cards
for rank in ranks:
  for suit in suits:
    deck.append(Card(rank, suit))

#Test # 1: Deal a hand for the player
#deal(deck, playerHand)
#deal(deck, playerHand)
#printHand(playerHand)
#print(handValue(playerHand))

#Test # 2: Testing if the ace test works
#print("Ace Test")
#aceHand = []
#aceHand.append(Card("Ace", "Clubs"))
#aceHand.append(Card("Ace", "Hearts"))
#aceHand.append(Card("Ace", "Spades"))
#aceHand.append(Card("Ace", "Diamonds"))

#printHand(aceHand)
#print(handValue(aceHand))

print("Welcome to Blackjack!")
name = input("Please Enter Your Name: ")
MrHouse = Player("Mr. House", 100000000)
playerOne = Player(name, 100)
print("Starting Funds:", playerOne.wallet)
pool = 0

print("Hello", name + ", welcome to the table!")
roundNumber = 1

def getBet(player):
  while True:
    newBet = int(input("Place your bet: "))
    if newBet > player.wallet:
      print("Insufficient Funds!")
    else:
      return player.wallet

def placeBet(player, newBet):
    player.wallet -= newBet
    player.bet = newBet
    print("Current bet:", player.bet)
    print("Remaining funds for", player.name + ":", player.wallet)
  

print("Round", str(roundNumber) + "!")
#Get the bets from the player
placeBet(playerOne, getBet(playerOne))
placeBet(MrHouse, playerOne.bet)

pool = playerOne.bet + MrHouse.bet
print("Current pool:", pool)

print("Dealing cards...")
#Deal two cards to the player
deal(deck, playerOne)
deal(deck, playerOne)

#Deal two cards to Mr House
deal(deck, MrHouse)
deal(deck, MrHouse)

#Prints the Player's Hand
printHand(playerOne)
print(playerOne.name + "'s Hand Value:", handValue(playerOne.hand))

#Prints the House's Hand
printHand(MrHouse)
print(MrHouse.name + "'s Hand Value:", handValue(MrHouse.hand))

#Ask the player to hit or stand
hitStand = input("Hit or Stand? ")
print(hitStand)

#If the player hit...
while hitStand == "hit":
  deal(deck, playerOne.hand)
  printHand(playerOne)
  print("Hand Value:", handValue(playerOne.hand))
  safeBust = checkValue(playerOne.hand)
  if safeBust == "Bust!":
    print("Player Bust!")
    break
  hitStand = input("Hit or Stand? ")
#otherwise...
else:
  pass











