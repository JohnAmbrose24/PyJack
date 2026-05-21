import random
#Lists of Ranks
ranks = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

#List of Suits
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

#The Card class object, containing a card's rank, suit and value. 
class Card(object):
  value = 0
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    self.value = ranks[rank]

  def setValue(self, newValue):
    self.value = newValue

#The Player class object, containing a player's wallet and current bet 
class Player(object):
  wins = 0
  losses = 0
  #bet = 0
  wallet = 0
  name = ""
  def __init__(self, name, wallet, hand):
    self.wallet = wallet
    self.name = name
    self.hand = hand


#Pops a card from the deck and adds it to the player's hand
#ERROR!!! The function is currently appending the card to both player's hands!
def deal(deck, player):
  newHand = player.hand
  newHand.append(deck.pop(random.randint(0, (len(deck) - 1))))
  player.hand = newHand
  return player.hand

#Prints a specific card's rank and suit
def printCard(card):
  print(card.rank + " of " + card.suit)

#Prints a hand using the printCard function
def printHand(player):
  hand = player.hand
  print(player.name + "'s Hand:")
  for card in hand:
    printCard(card)
  print(player.name + "'s Hand Value: ", realHandValue(hand))
      
#Calculates the total value of a given list of cards
def handValue(hand):
  total = 0
  for card in hand:
    total += card.value
  return total 

#Checks a hand for Aces that are being read as 11s, and changes them one-by-one until the hand is below 21.
def fixAce(hand):
  value = handValue(hand)
  if value > 21:
    #print("Trying to find an ace...")
    for i in range(len(hand)):
      #If the card is Ace and the value is 11...
      if hand[i].rank == "Ace" and hand[i].value == 11:
        #print("Fixing Ace...")
        hand[i].value = 1
        value = handValue(hand)
        if value < 22:
          return hand
  return hand

#Calls handValue and fixAce to get the proper
def realHandValue(hand):
  value = handValue(hand)
  #If the hand is above 21, fix the hand
  if value > 21:
    hand = fixAce(hand)
    value = handValue(hand)
  return value
  
#Returns Bust if the realHandValue of a hand is over 21, and Safe otherwise.
def checkValue(hand):
  value = realHandValue(hand)
  if value > 21:
    return "Bust!"
  else:
    return "Safe!"
  
#Prints out Player's Name, Wallet and Win/Loss ratio
def playerStats(player):
  print("Player Name: ", player.name)
  print("Chips: ", player.wallet)
  print("Win/Loss Ratio:", player.wins, "/", player.losses)

#Retrieves a bet from the player and checks to see if the bet is 
def getBet(player):
  while True:
    newBet = int(input("Place your bet: "))
    if newBet > player.wallet:
      print("Insufficient Funds!")
    else:
      print("Bet Placed!")
      return newBet

#Takes the set bet away from the player's wallet
def placeBet(player, bet):
    player.wallet -= bet
    player.bet = bet
    print("Current bet:", player.bet)
    print("Remaining funds for", player.name + ":", player.wallet)

#GAME RUNNING CODE
#Make the deck
deck = []
#Fill the deck with cards
for rank in ranks:
  for suit in suits:
    deck.append(Card(rank, suit))

#Returns 1 if the player busted, and 2 if the player didn't.
def playerBust(player):
  if realHandValue(player.hand) > 21:
    return True
  else:
    return False
#Returns 1 if the first player won, 2 if the second player won. If they equal each other and didn't bust, return 3.
def determineWinner(player1, player2):
  #If the Player Didn't Bust...
  if playerBust(player1) == False:
    #If the other player busted, or this hand is bigger than the other hand...
    if playerBust(player2) == True or realHandValue(player1.hand) > realHandValue(player2.hand):
      #Return 1
      return 1
    elif realHandValue(player1.hand) == realHandValue(player2.hand):
      return 3
  return 2

#Test # 2: Testing if the ace test works
#print("Ace Test")
#aceHand = []
#aceHand.append(Card("Ace", "Clubs"))
#aceHand.append(Card("Ace", "Hearts"))
#aceHand.append(Card("Ace", "Spades"))
#aceHand.append(Card("Ace", "Diamonds"))
#print(realHandValue(aceHand))

#The Game begins: the player inputs his name, we create two Player objects for the player and the "House", 
print("Welcome to Blackjack!")
name = input("Please Enter Your Name: ")
emptyHand = []
emptyHand2= []

MrHouse = Player("Mr. House", 100000000, emptyHand)
playerOne = Player(name, 100, emptyHand2)

print("Starting Funds:", playerOne.wallet)
pool = 0

print("Hello", name + ", welcome to the table!")
roundNumber = 1

#While the player has money...
while playerOne.wallet > 0:
  #State the Round Number
  print("Round", str(roundNumber) + "!")
  #Get the bets from the player
  placeBet(playerOne, getBet(playerOne))
  placeBet(MrHouse, playerOne.bet)
  pool = playerOne.bet + MrHouse.bet
  print("Current pool:", pool)
  input("Press Enter When Ready")
  print("Dealing cards...")

  #Deal two cards to the player
  deal(deck, playerOne)
  deal(deck, playerOne)

  #Deal two cards to Mr House
  deal(deck, MrHouse)
  deal(deck, MrHouse)

  #Prints the Player's Hand
  printHand(playerOne)

  #Prints the House's Hand
  printHand(MrHouse)

  hitStand = " "
  #If the Player didn't win outright
  if realHandValue(playerOne.hand) < 21:
    #Ask the player to hit or stand
    hitStand = input("Hit or Stand? ").lower()

  #If the player hit...
  while hitStand == "hit":
    #Deal the Player a new card, print the hand, then check to see if the player busted.
    deal(deck, playerOne)
    printHand(playerOne)
    print("Hand Value:", realHandValue(playerOne.hand))
    #If the player busted...
    if checkValue(playerOne.hand) == "Bust!":
      print("You Busted!")
      break
    hitStand = input("Hit or Stand? ")
  #otherwise...
  #else:
  if playerBust(playerOne) != 1:
    while realHandValue(MrHouse.hand) < 17:
      print("The House Hits...")
      deal(deck, MrHouse)
      printHand(MrHouse)
  
  print("Winner  =", determineWinner(playerOne, MrHouse))
  #Determines the Winner...
  if determineWinner(playerOne, MrHouse) == 1:
    print("YOU WIN!!")
    playerOne.wallet += pool
    playerOne.wins += 1
  elif determineWinner(playerOne, MrHouse) == 3:
    print("It's a Tie!")
    playerOne.wallet += pool / 2
    MrHouse.wallet += pool / 2
  else:
    print("The House Always Wins...")
    MrHouse.wallet += pool
    playerOne.losses += 1
  
  
  print("New Totals:")
  print(playerOne.name + "'s Balance: ", playerOne.wallet)
  print(MrHouse.name + "'s Balance: ", MrHouse.wallet)
  print("Resetting...")
  roundNumber += 1
  playerOne.hand.clear()
  MrHouse.hand.clear()
  pool = 0
  input("Press Enter When Ready: ")

print("Game Over!")
