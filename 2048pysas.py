from os import system,name
from time import sleep
def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
def  clear():
    _ = system('clear')
import getpass
import random
k=[]
me=[]
per=[]
def matrixsize():
    global n
    n=int(input("enter the size of matrix"))
    if n == 0:
        print("enter the no.greater than'0' ")
        matrixsize()
    return n
def callengenum():
    global p
    p=int(input("callenge no."))
    po=0
    while(p>2**po):
        po=po+1
    if p==0 or p!=2**po:
        print("enter the no.greater than'0'and no. must be power of '2' ")
        callengenum()
    return p
def myprint(k,n):
    for i in range(n):
        for j in range(n):
            print(k[i][j],"\t",end="")
        print()
def maxnum(k,n):
    global x
    x=0
    for i in range(0,n):
        for j in range(0,n):
            if k[i][j]>x:
                x=k[i][j]

    return x
def randomplace(k,n):
    global ajay
    global shah
    x=random.randrange(0,n)
    y=random.randrange(0,n)
    if k[x][y]==0:
        k[x][y]=2*random.randrange(1,3)
        ajay=x
        shah=y

    else:
        randomplace(k,n)
def move(k,n,dir):

    if dir=="d"or dir=="D":
        for i in range(n):
            for l in range(n):
                for j in range(n-l-1):
                    if(k[i][j]!=0 and k[i][j+1]==0):
                        temp=k[i][j+1]
                        k[i][j+1]=k[i][j]
                        k[i][j]=temp
        for i in range(n):
            for j in range(n):
                if k[i][n-1-j]==k[i][n-2-j]:
                    k[i][n-1-j]=2*k[i][n-1-j]
                    for p in range(0,n-j-2):
                        k[i][n-j-2-p]=k[i][n-j-3-p]
                    k[i][0]=0




    if dir=="a" or dir=="A":
         for i in range(n):
             for l in range(n):
                 for j in range(n-l-1):
                     if(k[i][j]==0 and k[i][j+1]!=0):
                         temp=k[i][j]
                         k[i][j]=k[i][j+1]
                         k[i][j+1]=temp
         for i in range(n):
             for j in range(n-1):
                 if k[i][j]==k[i][j+1]:
                     k[i][j]=2*k[i][j]
                     for p in range(j+1,n-1):
                         k[i][p]=k[i][p+1]
                     k[i][n-1]=0



    if dir=="w" or dir=="W":
         for i in range(n):
             for l in range(n-1):
                 for j in range(n-l-1):
                     if(k[j][i]==0 and k[j+1][i]!=0):
                         temp=k[j][i]
                         k[j][i]=k[j+1][i]
                         k[j+1][i]=temp
         for i in range(n):
             for j in range(n-1):
                 if k[j][i]==k[j+1][i]:
                     k[j][i]=2*k[j][i]
                     for p in range(j+1,n-1):
                         k[p][i]=k[p+1][i]
                     k[n-1][i]=0


    if dir=="s" or dir=="S":
         for i in range(n):
             for l in range(n-1):
                 for j in range(n-l-1):
                     if(k[j][i]!=0 and k[j+1][i]==0):
                         temp=k[j+1][i]
                         k[j+1][i]=k[j][i]
                         k[j][i]=temp
         for i in range(n):
             for j in range(n):
                 if k[n-1-j][i]==k[n-2-j][i]:
                     k[n-1-j][i]=2*k[n-1-j][i]
                     for p in range(0,n-j-2):
                         k[n-j-2-p][i]=k[n-j-3-p][i]
                     k[0][i]=0


    print("\n")
def getinput():
    dir=getch()
    return dir
condition="play"
while(condition=="play"):
    n=matrixsize()
    p=callengenum()
    h=[0]
    count=0
    for i in range(n):
        s=[]
        for j in range(n):
            s.append(0)
        k.append(s)
    while count<1:
        if  n==1:
            k[0][0]=2*random.randrange(1,3)
            myprint(k,n)
            if p==k[0][0]:
                print("congratulation you won")
                print("replay or quit")
                m=str(input())
                if m=="replay" or m=="REPLAY":
                    condition="play"
                    break
                else:
                    condition= "stop"
                    break
                break
            else:
                print("game over")
                print("replay or quit")
                m=str(input())
                if m=="replay" or m=="REPLAY":
                    condition="play"
                    break
                else:
                    condition= "stop"
                    break
                break
        if  n==2:
            x=random.randrange(0,n)
            y=random.randrange(0,n)
            k[x][y]=2
            count=count+1

        if n>2:
            for i in range(2):
                x=random.randrange(0,n)
                y=random.randrange(0,n)
                k[x][y]=2*random.randrange(1,3)
                count=count+1
    if n!=1:
        myprint(k,n)
    max=0
    index=0
    while p>max and n!=1:
        h=k
        dir=getinput()
        clear()
        move(k,n,dir)
        sushlok=0
        poco=0
        for i in range(n):
            for j in range(n):
                if k[i][j]==0:
                    sushlok=sushlok+1
                    poco=poco+1
        for i in range(n):
            for j in range(n-1):
                if k[i][j]==k[i][j+1]:
                    sushlok= sushlok+1
                if k[j][i]==k[j+1][i]:
                    sushlok=sushlok+1
        if h==k and sushlok==0:
            myprint(k,n)
            print("game over")
            print("replay or quit")
            m=str(input())
            if m=="replay" or m=="REPLAY":
                condition="play"
                break
            else:
                condition= "stop"
                break
        else :
            if dir=="w"or dir=="a" or dir=="s" or dir=="d" or dir=="W" or dir=="A" or dir=="S"or dir=="D":
                if poco!=0:
                    randomplace(k,n)
            else:
                print("invalid input")
        myprint(k,n)
        print("\n")
        max=maxnum(k,n)
        if p==max:
            print("congratulation you won")
            print("replay or quit")
            m=str(input())
            if m=="replay"or m=="REPLAY":
                condition="play"
            else:
                condition= "stop"
                break
