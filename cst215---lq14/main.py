import random
import copy
# import packages

# defining the function
def shuffleDeck(n):
    
    # Creating the base deck
    deck = []
    for i in range(n):
        deck.append(i+1)
        
    print("Original deck...")
    print(deck)
    
    # Creating the 1 and 2 copy of the deck
    deck1 = copy.copy(deck)
    random.shuffle(deck1)
    
    print("After first draw...")
    print(deck1)
    
    deck2 = copy.copy(deck)
    random.shuffle(deck2)
    
    print("After second draw...")
    print(deck2)
    
    # Compare the drawn decks
    fpCounter = 0
    for i in range(n):
        if (deck1[i] == deck2[i]):
            fpCounter += 1
    
    print("There are", fpCounter, " fixed points")
    
    
shuffleDeck(6)











