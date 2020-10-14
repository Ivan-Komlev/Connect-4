"""
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in Python.
Before you get started, please watch this video on the rules of Connect 4:

Author: Ivan Komlev
Date: 2020-10-14
GitHub: https://github.com/Ivan-Komlev/Connect-4
"""

import sys
from termcolor import colored, cprint
import os
from os import system
os.system('color')

bgColor='on_white'
xOffset=10

columns,rows =9,6

#player1name=""
#player2name=""

#Clear screen
print('\x1b[2J')

map = [[0 for i in range(columns)] for j in range(rows)] 
#map=[[0]*columns] * rows #Rows [Columns]
#0 = empty space
#1 = red player
#2 = green player

def printMapElement(r,c):
    #text = colored(' y:'+str(y)+" ", 'red')#, attrs=['reverse', 'blink']);
    if map[r][c]==1:
        cprint("  ", 'blue', "on_red", end="");
    elif map[r][c]==2:
        cprint("  ", 'blue', "on_green", end="");
    elif map[r][c]==-1:
        cprint("><", 'white', "on_red", end="");
    elif map[r][c]==-2:
        cprint("><", 'black', "on_green", end="");
    else:
        cprint("  ", 'blue', bgColor, end="");
    
    return
    
def findAvalableRow(c):
    for r in range(0,rows):
        row=rows-r-1
        if(map[row][c-1]==0):
            return row+1
        
    return -1;#column is full
    
def markBlocks(won_blocks,turn):
    for i in range(0,len(won_blocks)):
        map[won_blocks[i][0]][won_blocks[i][1]]=-turn
        
    return won_blocks
    
def checkIfWon(r,c,turn):# r=1:rows, c=1:columns
    
    r_=r-1 # to start from 0 not from 1
    c_=c-1 # to start from 0 not from 1
    
    #check horizontals
    won_blocks=[]
    count=0
    for c_ in range(0,columns):
        if(map[r_][c_]==turn):
            won_blocks.append([r_,c_])
            count+=1
            if count==4:
                won_blocks=markBlocks(won_blocks,turn)
                return True;
        else:
            count=0
            won_blocks=[]
            
            
    #check vertical
    c_=c-1 # to start from 0 not from 1
    won_blocks=[]
    count=0
    for r_ in range(0,rows):
        if(map[r_][c_]==turn):
            won_blocks.append([r_,c_])
            count+=1
            if count==4:
                won_blocks=markBlocks(won_blocks,turn)
                return True;
        else:
            count=0
            won_blocks=[]
    
    #check diagonals
    for r_ in range(0,rows-4+1):#rows-4 -------- dont check the imposible
        for c_ in range(0,columns-4+1):#columns-4 -------- dont check the imposible
            won_blocks=[]
            count=0
        
            #check diagonal left to right
            c2_=c_
            for r2_ in range(r_,r_+4):
                if(map[r2_][c2_]==turn):
                    print("r2_:"+str(r2_)+"c2_:"+str(c2_)+"Found")
                    won_blocks.append([r2_,c2_])
                    count+=1
                    if count==4:
                        won_blocks=markBlocks(won_blocks,turn)
                        return True;
                else:
                    count=0
                    won_blocks=[]
                c2_+=1
                if c2_==c_+4:
                    break
                
            won_blocks=[]
            count=0
            #check diagonal right to left
            c3_=columns-c_-1
            for r2_ in range(r_,r_+4):
                if(map[r2_][c3_]==turn):
                    won_blocks.append([r2_,c3_])
                    count+=1
                    if count==4:
                        won_blocks=markBlocks(won_blocks,turn)
                        return True;
                else:
                    count=0
                    won_blocks=[]
                
                c3_-=1
                if c3_<0:
                    break

    return False
    
    
def drawTheBoard(rows, columns_):

    columns=columns_*2-1
    
    #Drawing Column numbers
    print(" "*xOffset,end="")
    
    cprint("   ", 'blue', bgColor, end="")
    for j in range(0, columns):
        c=(str(int(j/2)+1)+" " if j%2==0 else ' ')
        cprint(c, 'blue', bgColor, end="")
    cprint("  ", 'blue', bgColor)
    
    #Drawing board top line
    print(" "*xOffset,end="")
    cprint("  "+u'\u250c', 'blue', bgColor, end="")#left top corner
    for j in range(0, columns):
        c=(u'\u2500'+u'\u2500' if j%2==0 else u'\u252C')
        cprint(c, 'blue', bgColor, end="")
        
    cprint(u'\u2510'+' ', 'blue', bgColor)
  
    
    for i in range(0, rows):
        print(" "*xOffset,end="")
        cprint(" "+str(i+1)+u'\u2502', 'blue', bgColor, end="")
        for j in range(0, columns):
            if j%2==0:
                printMapElement(i,int(j/2))
            else:
                cprint(u'\u2502', 'blue', bgColor, end="")
                
        cprint(u'\u2502'+' ', 'blue', bgColor)
        
        if i<rows-1:
            print(" "*xOffset,end="")
            cprint('  '+u'\u251C', 'blue', bgColor, end="")
            
            for j in range(0, columns):
                c=(u'\u2500'+u'\u2500' if j%2==0 else u'\u253C')#line or cross
                cprint(c, 'blue', bgColor, end="")
            
            cprint(u'\u2524'+' ', 'blue', bgColor)


    #Drawing board bottom line
    print(" "*xOffset,end="")
    cprint("  "+u'\u2514', 'blue', bgColor, end="")#left top corner
    for j in range(0, columns):
        c=(u'\u2500'+u'\u2500' if j%2==0 else u'\u2534')
        cprint(c, 'blue', bgColor, end="")
        
    cprint(u'\u2518'+' ', 'blue', bgColor)

    return True;




def rules():
    print("Welcome to the Connect 4 game.")
    print("Rules:")
    print("Enter the column you wish to drop your piece in.")
    print("When you can connect four pieces vertically, horizontally or diagonally you win")

    print("Type 'q' to exit the game.")

def prompter():
    turn=1

    #Rules
    
    while(True):
    
   
        color=("Red" if turn==1 else 'Green')
        cprint(color+" player, plase enter the column:", color.lower(), end="")
        
        column = input(" ")
        if column=="":
            cprint('Column is not a number', 'white', 'on_red')
            continue
            
        try:
            column=int(column)
        except (ValueError, TypeError):
            if(column=='q' or column=='Q'):
                break
            else:
                cprint('Column is not a number', 'white', 'on_red')
                continue
        
        column=int(column)
        
        if column>columns or column<1:
            cprint('Column number is outside of range', 'white', 'on_red')
            continue

        r=findAvalableRow(column)
        if r==-1:
            #Column is full
            cprint('Column is full', 'white', 'on_yellow')
        else:
            map[r-1][column-1]=turn
            
            if checkIfWon(r,column,turn):
                #Clear screen
                print('\x1b[2J')
                drawTheBoard(rows, columns)
                rules()
                cprint(color+' won!', 'blue', 'on_white', end="")
                break
        
            #Change player
            turn+=1
            if turn==3:
                turn=1
            
            #Clear screen
            print('\x1b[2J')
            drawTheBoard(rows, columns)
            rules()
            print()
        
drawTheBoard(rows, columns)
rules()
print()
prompter()

print("        Bye.")