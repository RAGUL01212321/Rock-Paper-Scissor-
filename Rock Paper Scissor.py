import random 
import time
import mysql.connector
choice=['yes','no']
print('''
********************************
           Welcome              
 Let's play Rock Paper Scissor
********************************''')
def player():
    input('enter your name:')
def choice():
    c=input('Are you ready (yes/no) :')
    return c.lower() 
def status():
    t=True
    yoimo=choice()
    while t==True:
        cho=['yes','no']
        if yoimo in cho:
            t=False
            if yoimo=='yes':
                intial()
                play()
            elif yoimo=='no':
                print('! ThankYou !')
        else:
            t=True
            print('!! enter a Valid Choice !!')
            yoimo=choice()
def intial():
    elements=['Rock','Paper','Scissor']
    for i in elements:
        time.sleep(1)
        print(i,end='\r')
        if i=='Scissor':
            time.sleep(1)
            print('Shoot !!')
def p():
    g=input('would you like to continue (y/n):')
    if g=='y' or g=='Y':
        status()
    else:
        print('Thankyou looser')
def play():
    r= ['Rock','Paper','Scissor']
    s=[0,1,2]
    h=['R','P','S']
    print(
        '''
        R - Rock
        P - Paper
        S - Scissor''')
    pl1=input('Enter your choice :')
    cc2=pl1.upper()
    if pl1=='R':
        pl1='Rock'
    elif pl1=='S':
        pl1="Sissors"
    else:
        pl1='Paper'
    cc1=random.choice(s)          
    print("Your choice : '{}'".format(pl1))
    print("Computer choice: '{}'".format(r[cc1]))
    if (cc2=='R' and h[cc1]=='R') or (cc2=='S' and h[cc1]=='S') or (cc2=='P' and h[cc1]=='P'):
        print('Draw, lets play again !')
        status()
    elif h[cc1]=='R' and cc2=='P': #1
        print('You WON !!!!! ')
        p()
    elif h[cc1]=='P' and cc2=='R': #2
        print('You LOST !!!!!')
        p()
    elif h[cc1]=='R' and cc2=='S': #3
        print('You LOST !!!!! ')
        p()
    elif h[cc1]=='S' and cc2=='R': #4
        print('You WON !!!!! ')
        p()
    elif h[cc1]=='P' and cc2=='S': #5
        print('You WON !!!!! ')
        p()
    elif h[cc1]=='S' and cc2=='P': #6
        print('You LOST !!!!! ')
        p()
status()
        
        