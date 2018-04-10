# BlackJack ♠	♥	♦	♣ https://en.wikipedia.org/wiki/Blackjack

import random

valueOfCards = {'2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

# card suits: hearts, diamonds, clubs, spades
suits = {'h':'♥','d':'♦','c':'♣','s':'♠'}

# Initial 'read-only' deck of 52 cards
initDeck = ['2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ah', \
            '2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ad', \
            '2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ac', \
            '2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','As']
#

# Deck of cards used for the game
deckOfCards = []

# (B) initDeckOfCards()
# Initialize a new deck for the game
def initDeckOfCards():
    global deckOfCards
    deckOfCards = initDeck
# (E) initDeckOfCards()

# Empty list with player's cards
player = []

# Empty list with computer's cards
comp = []

# Var used to store the value of a new card
newCard = None

# Visualization only
cardBack = '▒'

# Vars with player's and casino's funds
playerFunds = 0
casinoFunds = 0

# Bid value
bid = 50

# Current game fund
gameFund = 0

# Condition for while loop
playBlackJack = True

# (B) gameStart()
# The cards are dealt for the player & the computer
def gameStart():
    card1p = random.randint(0,52)
    card1p = deckOfCards[card1p]
    deckOfCards.remove(card1p)
    card1p = card1p[:-1] + suits[card1p[-1]]
    player.append(card1p)

    card1c = random.randint(0,51)
    card1c = deckOfCards[card1c]
    deckOfCards.remove(card1c)
    card1c = card1c[:-1] + suits[card1c[-1]]
    comp.append(card1c)

    card2p = random.randint(0,50)
    card2p = deckOfCards[card2p]
    deckOfCards.remove(card2p)
    card2p = card2p[:-1] + suits[card2p[-1]]
    player.append(card2p)
    
    card2c = random.randint(0,49)
    card2c = deckOfCards[card2c]
    deckOfCards.remove(card2c)
    card2c = card2c[:-1] + suits[card2c[-1]]
    comp.append(card2c)
# (E) gameStart()

# (B) playerCardsSuits()
# Human readable list of dealt cards (player)
def playerCardsSuits():
    tempList = []
    global player
    for card in player:
        tempList.append(card[:-1] + suits[card[-1]])
    player = tempList
# (E) playerCardsSuits()

# (B) sumOfCardsP()
# Number of points (player)
def sumOfCardsP():
    playerSum = 0
    if player[0] == player[1] == 'A':
        playerSum = 21
    else:
        for card in player:
            playerSum += valueOfCards[(card[:-1])]
    return playerSum
# (E) sumOfCardsP()

# (B) sumOfCardsC()
# Number of points (computer)
def sumOfCardsC():
    compSum = 0
    if comp[0] == comp[1] == 'A':
        compSum = 21
    else:
        for card in comp:
            compSum += valueOfCards[(card[:-1])]
    return compSum
# (E) sumOfCardsC()

# (B) printCardsP()
# Print the cards dealt and number of current points (player)
def printCardsP():
    pointsP = sumOfCardsP()
    print("You have such cards:")
    cardsText = ""
    for c in player:
        cardsText += c + " "
    print(cardsText)
    print("Your have " + str(pointsP) + " points.")
# (E) printCardsP()

# (B) printCardsC()
# Print the cards dealt and number of current points (computer)
def printCardsC():
    pointsC = sumOfCardsC()
    compTemp = ""
    for c in comp:
        compTemp += c + " "
    print("Computer has following cards: " + compTemp)
    print("It has " + str(pointsC) + " points.")
# (E) printCardsC()

# (B) money()
# Ask the user how much he/she is ready to 'spend'
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
def money():
    global playerFunds, casinoFunds
    while True:
        try:
            playerFunds = int(input("How much money are you ready to deposit? (Minimum bid is 50!) "))
            casinoFunds = playerFunds * 2
        except ValueError:
            print("Type only digits and hit [Enter]: ")
            continue
        else:
            break
# (E) money()

# (B) startGame()
# Play the game until one of the sides is out of funds.
# Or the player decides to quit
def startGame():
    global playBlackJack
    print("You deposit is " + str(playerFunds) + " now.")
    print("Casino funds are " + str(casinoFunds) + " now.")
    if playerFunds <= 0:
        print("You are a loser!")
        exit()
    elif casinoFunds <= 0:
        print("Casino has lost :(")
        exit()
    playAgain = input("Do you want to play? 'y' - yes, 'n' - no: ")
    if playAgain == 'n':
        print("Bye!")
        exit()
    elif playAgain == 'y' or playAgain == '':
        #deckOfCards = initDeck
        initDeckOfCards()
        player.clear()
        comp.clear()
    else:
        print("Please, use 'y' or 'n' letters only!")
# (E) startGame()

# (B) playGame()
# The game itself
def playGame():
    global gameFund, playerFunds, casinoFunds, playBlackJack
    gameFund = bid + bid
    playerFunds -= bid
    casinoFunds -= bid
    print("Current bank is " + str(gameFund))
    print("Computer has following cards: " + comp[0] + " " + cardBack)
    printCardsP()
    condition = True
    while condition and playBlackJack:
        deckOfCards = initDeck
        user = input("What is your move? 'h' - hit, 's' - stand, 'd' - double, 'u' - surrender, '?' - help: ")
        if user == 'h':
            newCard = deckOfCards[random.randint(0,len(deckOfCards))]
            deckOfCards.remove(newCard)
            newCard = newCard[:-1] + suits[newCard[-1]]
            player.append(newCard)
            printCardsP()
            summaP = sumOfCardsP()
            print(summaP)
            if summaP > 21:
                print("You lost! Sorry!")
                casinoFunds += gameFund
                condition = False
            elif summaP == 21:
                print("You WON!")
                playerFunds += gameFund
                printCardsP()
                condition = False
            elif summaP == sumOfCardsC():
                print("It's a draw!")
                playerFunds += gameFund / 2
                casinoFunds += gameFund / 2
                printCardsP()
                condition = False
        elif user == 's':
            playerSum = sumOfCardsP()
            compSum = sumOfCardsC()
            printCardsC()
            while compSum < 17:
                newCard = random.randint(0,len(deckOfCards))
                newCard = deckOfCards[newCard]
                deckOfCards.remove(newCard)
                newCard = newCard[:-1] + suits[newCard[-1]]
                comp.append(newCard)
                compSum += valueOfCards[newCard[:-1]]
            else:
                if (compSum > 21) or (compSum < playerSum):
                    print("You won!")
                    playerFunds += gameFund
                    printCardsC()
                    condition = False
                elif compSum > playerSum:
                    print("You lost! Sorry!")
                    casinoFunds += gameFund
                    printCardsC()
                    condition = False
                if compSum == playerSum:
                    print("Wow! It's a draw...")
                    playerFunds += gameFund / 2
                    casinoFunds += gameFund / 2
                    printCardsC()
                    condition = False
        elif user == 'd':
            playerSum = sumOfCardsP()
            compSum = sumOfCardsC()
            gameFund += bid
            playerFunds -= bid
            newCard = deckOfCards[random.randint(0,len(deckOfCards))]
            deckOfCards.remove(newCard)
            playerSum += valueOfCards[newCard[:-1]]
            player.append(newCard[:-1] + suits[newCard[-1]])
            printCardsP()
            if playerSum > 21:
                print("You lost your double bet!")
                casinoFunds += gameFund
                printCardsC()
                print("You deposit is " + str(playerFunds) + " now.")
                print("Casino funds are " + str(casinoFunds) + " now.")
                condition = False
            elif (playerSum == 21) and (compSum != 21):
                print("You won the double bet!")
                playerFunds += gameFund
                printCardsC()
                print("You deposit is " + str(playerFunds) + " now.")
                print("Casino funds are " + str(casinoFunds) + " now.")
                condition = False
            elif playerSum > compSum:
                print("You won! Hurray!")
                playerFunds += gameFund
                printCardsC()
                print("You deposit is " + str(playerFunds) + " now.")
                print("Casino funds are " + str(casinoFunds) + " now.")
                condition = False
            elif playerSum < compSum:
                print("Oops... You lost your double bet!")
                casinoFunds += gameFund
                printCardsC()
                print("You deposit is " + str(playerFunds) + " now.")
                print("Casino funds are " + str(casinoFunds) + " now.")
                condition = False
        elif user == 'u':
            print("Bad luck, it happens.")
            playerFunds += bid / 2
            casinoFunds += gameFund - bid / 2
            print("You deposit is " + str(playerFunds) + " now.")
            print("Casino funds are " + str(casinoFunds) + " now.")
            condition = False
        elif user == 'q':
            print("Good-bye! We'll miss you and your money!")
            playBlackJack = False
        elif user == '?':
            print("Help:")
            print("h -> 'hit' - take a card;")
            print("s -> 'stand' - end turn;")
            print("d -> 'double' - double wager, take a single card and finish;")
            print("u -> 'surrender' - give up a half-bet and retire from the game;")
            print("q -> 'quit' - quit game.")
        else:
            print("Sorry, I didn't understand you.")
    #else:
        #deckOfCards = initDeck
# (E) playGame()

# Let's start
money()
print(playerFunds)


# While loop
while playBlackJack:
    startGame()
    initDeckOfCards()
    gameStart()
    playGame()