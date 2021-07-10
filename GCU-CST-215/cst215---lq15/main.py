import random
import copy
# import packages

# defining the function
def shuffleDeck(n, times):
    
    # Creating the base deck
    deck = []
    for i in range(n):
        deck.append(i+1)
        
    print("Deck of", n, "cards...", times, "different card selections")
    print("Fixed Pts\tPercentage")
    print("--------------------------")
    
    
    
    fpArray = [None] * 10
    
    for j in range(times):
        fpCounter = 0
        # Creating the 1 and 2 copy of the deck
        deck1 = copy.copy(deck)
        random.shuffle(deck1)
        

        deck2 = copy.copy(deck)
        random.shuffle(deck2)
        

        # Compare the drawn decks
        for i in range(n):
            if (deck1[i] == deck2[i]):
                fpCounter += 1
        
        if fpArray[fpCounter] == None:
            fpArray[fpCounter] = 1
        else:
            fpArray[fpCounter] += 1
        
    for k in range(10):
        if fpArray[k] == None:
            fpArray[k] = 0
        print(k,"\t\t", fpArray[k]/times)
    print(fpArray)
    
shuffleDeck(100, 1000)












