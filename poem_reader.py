def countdot():
    with open("poem.txt","r") as p:
        data=p.read()
        count=0
        for i in data:
            if i == ".":
                count+=1
        return count
def wordI():
    with open("poem.txt","r") as p:
        data = p.read()
        count=0
        word=data.split()
        for i in word:
            if i == "I":
                count+=1
        return count
def linesT():
    with open("poem.txt","r") as p:
        data=p.readlines()
        for i in data:
            if i[0] in "tT":
                print(i,end='')
def firstlast():
    with open("poem.txt", "r") as p:
        data = p.readlines()
        for i in range(-1,-2):
            print(i,end='')
        for i in range(1,2):
            print(i,end='')
def longline():
    with open("poem.txt", "r") as p:
        data = p.readlines()
        longest = ("")
        for i in data:
            word = p.readline()
            words = word.split(i)
            if len(i) > len(longest):
                longest=i
        return print(longest)
while True:
    print('\n=====      MENU       =====')
    print('''1. Count no of dots '.'
2. Count word ‘I’
3. Display lines starting with ‘tT’
4. Display the firts & last line 
5. Display the longest line
0. Exit
=======================================''')

    ch = int(input('Enter your choice : '))
    if ch == 1:
        print('No of times "."  appears = ', countdot())
    elif ch == 2:
        print('No of times word "I" appears = ', wordI())
    elif ch == 3:
        linesT()
    elif ch == 4:
        firstlast()
    elif ch == 5:
        longline()
    elif ch == 0:
        exit()
    else:
        print('Wrong choice')