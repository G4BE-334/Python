# Defining the function
def CaesarCypher(shiftV):
    
    with open('text.txt', 'r') as file:
        # Loop through all the lines in the file
        for line in file:
            # Loop through all the letters in the file
            for char in line:
                #If the letter is upper case convert it to lower case
                if (char.isupper()):
                    char = char.lower()
                
                # Encrypting the text
                # isalpha is used to only consider letter, not punctuation 
                if(char.isalpha()):
                    result = chr((ord(char) + shiftV - 97) % 26 + 97)
                else:
                    result = char
                
                # We set end = '' because python by default jumps to the next line after every print
                print(result, end = '')
                
CaesarCypher(10)