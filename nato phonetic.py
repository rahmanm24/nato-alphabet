#Alphabet List. Key = English Alphabet, Value = Nato Alphabet
nato = {
    "a" : "Alpha",
    "b" : "Bravo",
    "c" : "Charlie",
    "d" : "Delta",
    "e" : "Eco",
    "f" : "Foxton",
    "g" : "Golf",
    "h" : "Hotel",
    "i" : "India",
    "j" : "Juliet",
    "k" : "Kilo",
    "l" : "Lima",
    "m" : "Mike",
    "n" : "November",
    "o" : "Oscar",
    "p" : "Papa",
    "q" : "Quebec",
    "r" : "Romeo",
    "s" : "Sierra",
    "t" : "Tango",
    "u" : "Unform",
    "v" : "Victor",
    "w" : "Whiskey",
    "x" : "X-Ray",
    "y" : "Yankee",
    "z" : "Zulu" 
}

#function to convert into nato alphabet
def toNato():
    name = input("Enter your name: ")
    name = name.casefold()
    print("Your name in Nato Phonetic Format: ", end="")
    for alphabet in name:
        print(nato[alphabet], end=" ")
    print()

#function to convert nato alpabet into english alphabet
def fromNato():
    print("Please enter each word start with caps")
    name = list(map(str, input().strip().split()))  #take multiple input into a list in a single line separated by spaces 
    print("Your name in Nato Phonetic Format: ", end="")
    for alphabet in name:
        for key, value in nato.items():
            if alphabet == value:
                print(key, end="")
    print()
while True:
    c = int(input("Enter Your Choice\n1: Convert to nato\n2: Convert from nato\nor 0 to exit - "))
    if c == 0:
        break
    elif c == 1:
        toNato()
        print("\n")
    elif c == 2:
        fromNato()
        print("\n")
        
