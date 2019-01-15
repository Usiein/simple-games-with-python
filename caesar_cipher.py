# Caesar cipher

MAX_KEY_SIZE = 26

def getMode():
    while True:
        mode = input("Do you wish to encrypt or decrypt message?").lower()
        if mode in "encrypt e decrypt d".split():
            return mode
        else:
            print("Enter encrypt or e / decrypt or d")

def getMessage():
    return input("Input your message: ")

def getKey():
    key = 0
    while True:
        print("Enter the Key (1 - %s)" % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print("Your translated text is: ")
print(getTranslatedMessage(mode, message, key))      
