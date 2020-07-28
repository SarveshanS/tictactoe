#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time

class TicTacToe:
    
    
    def __init__(self, board, count , winner, play, tie, current_player, player_details ):
        print ("Currently inside the TictacTie initialization constructor")
        self.board = board;  #<---- Initalize: x = some passed vaiable; initialization == self.x
        self.count = count;
        self.winner = winner;
        self.play = play;
        self.tie = tie;
        self.current_player = current_player;
        self.player_details = player_details;
        
    # Helper functions
    def get_player_Info(self,curr_player):
        #Function to get the player's identifier and marker
        if curr_player == 'A':
            return ['B','O'] #<--- ['player identifier; e.g. A/B', 'player marker']
        else:
            return ['A','X']
        
    def print_tictactoeDisplayBoard(self):
        # Function to print the board
        for i in self.board:
            print( i, ':', self.board[i], ' ', end='')
            if i%3 == 0:
                print()
    
    
    def check_if_any_player_won(self, marker, player_id):
        # This function contains all of the winning combinations and checks to see if any of the players have 'achieved' them
        if self.board[1] == marker and self.board[2] == marker and self.board[3] == marker or \
        self.board[4] == marker and self.board[5] == marker and self.board[6] == marker or \
        self.board[7] == marker and self.board[8] == marker and self.board[9] == marker or \
        self.board[1] == marker and self.board[4] == marker and self.board[7] == marker or \
        self.board[2] == marker and self.board[5] == marker and self.board[8] == marker or \
        self.board[3] == marker and self.board[6] == marker and self.board[9] == marker or \
        self.board[1] == marker and self.board[5] == marker and self.board[9] == marker or \
        self.board[3] == marker and self.board[5] == marker and self.board[7] == marker:
    
            self.print_tictactoeDisplayBoard()
            time.sleep(1) #<-- Waits one second
            print("Player", player_id, "wins!")
            return True
    
        else:
            return False
    
    
    def select_location_by_player(self, slot_num, marker):
        print("Slot Number = " + str(slot_num))
        print("Marker = " + str(marker))
        # This function checks user inputs to see if they've already been taken; if not the locatino is 'marked'
        while self.board[slot_num] != ' ':
            print("This location has been taken; please pick a different location:")
            slot_num = int(input())
        self.board[slot_num] = marker #<--- Initialized
    
    def play_again(self):
#       # This function checks if the players want to play again
        print("Would you like to play again?")
        play_again = input()
    
        if play_again.upper() == 'Y':
            for z in self.board:
                self.board[z] = ' '
            return True
        else:
            print("Thank you for playing Tic Tac Toe! Stop by anytime!")
            return False
        
        
        