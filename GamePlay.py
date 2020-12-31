def random():
    import random
    pattern = []
    original = ['R','B','G','P','O','W','Y','V']
    random.shuffle (original)
    for i in range(0,4):
        pattern.append(original.pop())
    return pattern

def randomwithdup():
    import random
    pattern = []
    while len(pattern) <= 3:
        pattern.append(random.choice('RBGPOWYV'))
    return pattern

def checking(player):
    colorlist = set(['R','B','G','P','O','W','Y','V'])
    if set(player).issubset(colorlist) == False or len(player) != 4:
        return False
    else:
        return True
    
def trialtest(trying):
    trying = input("How many guess do you want? (1 - 9): ")
    while True:
        if not trying.isdigit():
            trying = input("Input must be numeric. Please type correctly: ")
        elif not 1 <= int(trying) <= 9:
            trying = input("Out of range. Please type correctly: ")
        else:
            return trying
            break

def playerplaying():
    from copy import copy
    redball = 0
    trial = 0
    startpoint = 1
    starting = 0
    trial = int(trialtest(trial))
    kang = [['_'] * 4 for i in range(trial)]
    listforball = [[0] * 2 for i in range(trial)]
    print ('\n' * 100)
    
    for x,y,z,w in kang:
        print (startpoint, x, y, z, w, listforball[starting])
        startpoint += 1
        
    while redball != 4 and trial != 0:
        print(" ")
        print ("Colors are R(ed), B(lue), G(reen), P(ink), O(range), W(hite), Y(ellow), V(iolet)")
        playerguess = list(input("Now guess the pattern: "))
        
        while checking(playerguess) == False:
            playerguess = list(input("Please type correctly: "))
            
        redball = 0
        whiteball = 0
        copycat = copy(pattern)
        copydog = copy(playerguess)
        
        for i in range(len(pattern)):
            if playerguess[i] == pattern[i]: 
                redball += 1
                copycat[i] = '@'
                playerguess[i] = '*'
                
        for i in range(len(pattern)):
            if playerguess [i] in copycat:
                whiteball += 1
                copycat.remove(playerguess[i])
                
        print ('\n' * 100)
        kang[starting] = copydog
        listforball[starting] = [redball, whiteball]
        startpoint = 1
        
        for x,y,z,w in kang:
            print (startpoint, x, y, z, w, listforball[startpoint - 1])
            startpoint += 1
        starting += 1
        
        print (" ")
        print ("Correct Position + Color: ", redball)
        print ("Correct Color: ", whiteball)
        trial -= 1
        
        if trial != 0 and redball != 4:
            print ("You have", trial, "guess left")
            
    if redball == 4:
        print (" ")
        print ("You won the game! The pattern was: ", pattern)
        
    elif trial == 0:
        print (" ")
        print ("You lost the game! The pattern was: ", pattern)

start = input('''If you want to play alone, please enter 1.
If you want to play Player vs Player, please enter 2: ''')

while True:
    if start == '1':
        level = input("Allow duplicates? yes/no: ")
        while True:
            if level == 'yes':
                pattern = randomwithdup()
                break
            elif level == 'no':
                pattern = random()
                break 
            else:
                level = input("Please type correctly. yes/no: ")
        playerplaying()
        break
    
    elif start == '2':
        colorlists = ['R','B','G','P','O','W','Y','V']
        print (" ")
        print ("Colors are R(ed), B(lue), G(reen), P(ink), O(range), W(hite), Y(ellow), V(iolet)")
        playervsplayer = input("Type the pattern you want to make: ")
        while checking(playervsplayer) == False:
            playervsplayer = input("Please type correctly: ")
        pattern = list(playervsplayer)
        playerplaying()
        break
    
    else:
        start = input("Please type correctly: ")
