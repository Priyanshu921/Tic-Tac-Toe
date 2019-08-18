#Programmer="Priyanshu Patidar"
"""
Note:-
This game is in the easy mode and hence the cpu will let you win by putting his variable in random places
"""
import time 
import numpy as brd
import random
import sys
computer=1
board = brd.array([0,0,0,0,0,0,0,0,0])
step=0
select=2
def isFull():
    if((board[0]==1 or board[0]==2) and (board[1]==1 or board[1]==2) and (board[2]==1 or board[2]==2) and (board[3]==1 or board[3]==2) and (board[4]==1 or board[4]==2) and (board[5]==1 or board[5]==2) and (board[6]==1 or board[6]==2) and (board[7]==1 or board[7]==2) and (board[8]==1 or board[8]==2)):
        return True
    else:
        return False
        
def yehraha():
    print("\n")
    print(board[0],"\t",board[1],"\t",board[2],"\n")
    print(board[3],"\t",board[4],"\t",board[5],"\n")
    print(board[6],"\t",board[7],"\t",board[8],"\n")
    print("\n")

def chance():
    
    global choice
    choice=random.randint(0,1)
    if(choice==1):
        return True
    else:
        return False
    
def selection():
    global select,computer
    select=int(input("1 or 2"))
    if(select==1):
       computer=2
    if(select==2):
       computer=1
    return select

def isValid(x):
    if(board[x]==0):
        return True
    else:
        return False
def isEmpty():
    if brd.all(board ==0):
        return True
    else:
        return False
    
def row_win(k):
    if(board[0]==k and board[1]==k and board[2]==k) or (board[3]==k and board[4]==k and board[5]==k) or (board[6]==k and board[7]==k and board[8]==k):
        return True    
    else:
        return False
    
def diag_win(k):
    if(board[0]==k and board[4]==k and board[8]==k) or (board[2]==k and board[4]==k and board[6]==k):
        return True
    else:
        return False
    
def col_win(k):
    if(board[0]==k and board[3]==k and board[6]==k) or (board[1]==k and board[4]==k and board[7]==k) or (board[2]==k and board[5]==k and board[8]==k):
        return True    
    else:
        return False
    
def pturn():
    global select
    x=int(input("Enter the block number to put "+str(select)))
    print("\n")
    if(isValid(x)):
        board[x]=select
    else:
        print("Enter a valid Number (Between 0 and 8)")
        print("\n")
        pturn()
    
def cturn():
    y=int(random.randint(0,8))
    if(isValid(y)):
        board[y]=computer
    else:
        cturn()
    
    
def playtime():
    global step
    while(not isFull()):
        if(choice==1):
            if( isFull()):
                print("Game is tied")
                sys.exit()
            pturn()
            step+=1
            print("after"+str(step)+"steps")
            yehraha()
            if(row_win(select) or col_win(select) or diag_win(select)):
                print("The Winner is player")
                sys.exit()
            time.sleep(1)
            
            time.sleep(1)
            if( isFull()):
                print("Game is tied")
                sys.exit()
            cturn()
            step+=1
            print("after"+str(step)+"steps")
            yehraha()
            
            if(row_win(computer) or col_win(computer) or diag_win(computer)):
                print("The Winner is computer")
                sys.exit()
        else:
            if( isFull()):
                print("Game is tied")
                sys.exit()
            time.sleep(1)
            cturn()
            step+=1
            print("after"+str(step)+"steps")
            yehraha()
            if(row_win(computer) or col_win(computer) or diag_win(computer)):
                print("The Winner is computer")
                sys.exit()
            
            if( isFull()):
                print("Game is tied")
                sys.exit()
            time.sleep(1)
            pturn()
            time.sleep(1)
            step+=1
            print("after"+str(step)+"steps")
            yehraha()
            if(row_win(select) or col_win(select) or diag_win(select)):
                print("The Winner is player")
                sys.exit()
           
def game():
    yehraha()
    player=selection()
    print("you selected:-"+str(player))
    print("Thus the computer will select:-"+str(computer))
    turn=chance()
    if(turn):
        time.sleep(1)
        print("Its Your Turn First")
    else:
        print("Its Computer's turn First")
    playtime()



game()
