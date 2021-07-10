# Defining the function
def VigenereCypher(key, textFile):
    
    # Transform key to lowercase
    key = key.lower()
    
    # Initiate the variable
    result = ""
    i = 0
    
    print("Original text...")
    with open(textFile, 'r') as file:
        
        # Loop through all the lines in the file
        for line in file:
            # Loop through all the letters in the file
            for char in line:
                
                #If the letter is upper case convert it to lower case
                if (char.isupper()):
                    char = char.lower()
                print(char, end = "")
                
                while i >= len(key):
                    i = i - len(key)
                    
                # Encrypting the text
                # isalpha is used to only consider letter, not punctuation 
                if(char.isalpha()):
                    char = chr((ord(key[i]) + ord(char) - 194) % 26 + 97)
                    i += 1
                result = result + char
                
                # We set end = '' because python by default jumps to the next line after every print
            print("\n")
        print("Encoded text...")
        print(result)
    print("\n")   
    
# Decripting
def VigenereDecryption(key):
    
    # Transform key to lowercase
    key = key.lower()
    
    print("Decoded text...")
    j = 0
    
    result = input()
    
    for ch in result:
        
        while j >= len(key):
            j = j - len(key)
            
        # Decripting the text
        if(ch.isalpha()):
            decoded = chr((ord(ch) - ord(key[j])) % 26 + 97)
            j += 1
        else:
            decoded = ch
            
        print(decoded, end = '')
        
VigenereCypher('Lemon', "text.txt")
VigenereDecryption('Lemon')





















