# py2048
 <h1>2048 python                                                                    code explanation</h1>
 
 
 
<b>from os import system,name</b>

imports system name and os and useful in giving cammands to the terminal


<b>from time import sleep</b>
 
used for stoping cammand from system for specific time


<b>import msvcrt</b>

library for windows for geting single char. from terminal(cmd)

<pre><b>def getch():<br />
        import sys <br />
        import tty <br />
        import termios <br />
        fd = sys.stdin.fileno() <br />
        old = termios.tcgetattr(fd) <br />
        try: <br />
            tty.setraw(fd) <br />
            return sys.stdin.read(1) <br />
        finally: <br />
            termios.tcsetattr(fd, termios.TCSADRAIN, old) <br /></b></pre>

used for getting single char. from terminal (linux and mac)

<pre><b>def  clear(): <br />
    if name =="nt": <br />
        _ =system('cls') <br />
    else: <br />
        _ = system('clear') <br /></b></pre>

for clearing terminal screen
<br />
import random

standard library for getting random number supporting different functions for random no.

<pre><b>def matrixsize(): <br />
    global n <br />
    n=int(input("enter the size of matrix")) <br />
    if n == 0: <br />
        print("enter the no.greater than'0' ") <br />
        matrixsize() <br />
    return n <br /></b></pre>

function defined for getting matrix size


<pre><b>def callengenum(): <br />
    global p <br />
    p=int(input("callenge no.")) <br />
    po=0 <br />
    while(p>2**po): <br />
        po=po+1  <br />
    if p==0 or p!=2**po: <br />
        print("enter the no.greater than'0'and no. must be power of '2' ") <br />
        callengenum() <br />
    return p <br /></b></pre>

function for getting challenged no.

<pre><b>def myprint(k,n): <br />
    for i in range(n): <br />
        for j in range(n): <br />
            print(k[i][j],"\t",end="") <br />
        print() <br /></b></pre>

function for printing matrix of given size


<pre><b>def maxnum(k,n): <br />
    global x  <br />
    x=0 <br />
    for i in range(0,n): <br />
        for j in range(0,n): <br />
            if k[i][j]>x:<br />
                x=k[i][j] <br />
<br />
    return x<br /></b></pre>

function for finding maximum number from matrix k

<pre><b>def randomplace(k,n): <br />
    global ajay <br />
    global shah <br />
    x=random.randrange(0,n) <br />
    y=random.randrange(0,n) <br />
    if k[x][y]==0: <br />
        if n==2:<br />
            k[x][y]=2 <br />
        else:<br />
            k[x][y]=2*random.randrange(1,3) <br />
        ajay=x <br />
        shah=y <br />
<br />
    else:<br />
        randomplace(k,n)<br /></b></pre>


function for placing 2 or 4 at random place in matrix


def move(k,n,dir):
    global z
    z=[]
    for i in range(n):
        s=[]
        for j in range(n):
            s.append(k[i][j])
        z.append(s)

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
    global check
    check=0
    if z==k:
        check=check+1

    print("\n")


function which takes input fromdir and moves the element of matrix
on input  w,a,s,d

<pre>def getinput():
    if name =="nt":
        dir=msvcrt.getch()
        char=dir[0]
        dir=chr(char)
    else:
        dir=getch()
    return dir</pre>

function for getting input (w,a,s,d)



<h1>working of code</h1>

1)enter the command “python 2048pysas.py” in terminal <br />
2)enter the matrix size<br />
 <img src="images/Screenshot_2020-05-17_08-35-33.png" >
3)enter the challenge no <br />
 <img src="images/Screenshot_2020-05-17_08-36-04.png" >

4)it will check whether it is power of 2 and no. is greater than 0.<br />
  else it will call again function <br />
 <img src="images/Screenshot_2020-05-17_08-36-38.png" >
  <img src="images/Screenshot_2020-05-17_08-36-58.png" >
5) after getting the terms it will display matrix with random 2’s or 4’s <br />
   for matrix of size "1" it will take input and it will compare the given no. with the random no. and then it will display "win" condition if given no. is same as the random no. 
  <img src="images/Screenshot_2020-05-17_08-38-16.png" >
6) depending upon direction move function will move the matrix <br />
 
inputs example <br />

d <br />
<img src="images/Screenshot_2020-05-17_09-00-19.png" >

d <br />
<img src="images/Screenshot_2020-05-17_09-00-36.png" >
same like that process continues untill you get “game over ” or “you won” <br />
it will ask “replay” or “quit” <br />
<img src="images/Screenshot_2020-05-17_09-10-03.png" >
<img src="images/Screenshot_2020-05-17_09-10-31.png" >
<img src="images/Screenshot_2020-05-17_09-11-20.png" >
<img src="images/Screenshot_2020-05-17_09-11-56.png" >
