#!/usr/bin/python

class toeboard(object):
    #initial variables 
    def __init__(self):
        #stores board as [row][column]
        self.state = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        #stores who goes next player1 = True, player2 = False(p2 = computer when applicable)
        self.pturn = True
    
    #clear the board when a game is over 
    def clear(self):
        self.state = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    def printState(self):
        #prints the board with a border
        #probably not the proper way to only show one board at a time.
        print ('\n' * 75)
        print ('+' + ('-' * 3) + '+')
        for i in self.state:
            row = "|"
            for k in i:
                row = row + k
            print (row + '|')
        print ('+' + ('-' * 3) + '+')
       

    def getUserInput(self):
        number = raw_input('> ').strip()
        try:
            #turn to number
            number = int(number)
            if number >= 1 and number <= 9:
                return number 
            else: 
                print("That number was out of the boundaries specified, please enter one between 1 and 9.")
                return self.getUserInput()

        except:
            #try again if failed before
            print ("That was not recognized as a number, please enter one.")
            return self.getUserInput() 

    def playGame(self):
        print ("Would you like to play a game vs:\n  1. Other Player\n  2. Computer\n")
        gamemode = raw_input("> ")
        if gamemode.strip() == '1':
            self.pvp("Player 1's turn. Press a number on the keypad that corresponds with he space you would like to take.") 
        else:
            self.ai()

    def checkWin(self):
         
        #checks rows for matching
        for w in self.state:
            if (w[0] == w[1] == w[2]) and w[0] != ' ':
                return True
        
        #checks columns for matching
        for e in range(0,3):
            if (self.state[0][e] == self.state[1][e] == self.state[2][e]) and self.state[0][e] != ' ':
                return True
            
        #check diagonals
        if (self.state[0][0] == self.state[1][1] == self.state[2][2]) and self.state[0][0] != ' ':
            return True
        elif (self.state[0][2] == self.state[1][1] == self.state[2][0]) and self.state[0][2] != ' ':
            return True

        return False
               
    #to grid format: turns numpad n into self.state[x][y]
    def playTurn(self, num ):
        #finds row/column by sorting by threes, then doing modulus
        row=0
        if num <4:
            row = 2
        elif num < 7:
            row = 1
        else: 
            row = 0
        
        num = num % 3
        if num == 0:
            num = 3
        num -= 1

        #enters data into toeboard, returns False if unsuccessful
        if self.state[row][num] == ' ':
            if self.pturn:
                self.state[row][num] = 'X' 
            else:
                self.state[row][num] = 'O'
                
            return True
        else:
            return False

    #function to insert X, O into table. return true if successful, false otherwise 
    def replace(self, spot, player):
        if spot == ' ':
            spot = player
            return True
        else:
            return False

    #recursive function: calls itself until game is finished.
    #play 2 player game   
    def pvp(self, msg):
        print (msg) 
        play = self.getUserInput()
        successful = self.playTurn(play)
        if not(successful):
            self.pvp("Spot is already taken, please input another.")
            return False
        else:
            self.pturn = not(self.pturn)
            self.printState()

        if self.checkWin():
            self.clear()
            print ('+' + '-' * 18 + '+')
            if self.pturn:
                print ("| Player 2 wins!!! |")
            else:
                print ("| Player 1 wins!!! |")
            print ('+' + '-' * 18 + '+')
        else:
            if self.pturn:
                self.pvp("Player 1's turn.")
            else:
                self.pvp("Player 2's turn.")

