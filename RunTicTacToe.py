#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from ProjectTicTacToe import TicTacToe

tactactoeDisplayBoard = {   1 : ' ', 2 : ' ', 3 : ' ',
                            4 : ' ', 5 : ' ', 6 : ' ', 
                            7 : ' ', 8 : ' ', 9 : ' '}
    
# Initialize variables
count = 0		    # <--- This is the counter to track the number of filled slots
winner = False		# <--- This is the boolean to check if one of the players won
play = True		    # <--- This is the boolen to check if the game should continue/not
tie = False		    # <--- This is the boolean to check if there is a tie in the game
current_player = ''	# <--- This is the variable storing the 'current player' identifier
player_details = []	# <--- This is the list storing the player identifier and marker
    
    

# This is the main program:
while play:

    # Creating the TicTacToe object passing all the various attributes of the game
    ticTacToe = TicTacToe(tactactoeDisplayBoard, count , winner, play, tie, current_player, player_details )

    ticTacToe.print_tictactoeDisplayBoard();

    # Getting the information from each player
    # When no player is passed, it returns['A','X']
    # The 1st item in the list is the Player & 2nd is the marker for the player
    # [Player] A , [Marker] X
    # [Player] B, [Marker]  O
    print("Current Player = " + current_player)
    player_details = ticTacToe.get_player_Info(current_player)
    current_player = player_details[0]
    input_location=0
    numbers=['1','2','3','4','5','6','7','8','9']
    while input_location not in numbers:
        input_location=input(f"Player {current_player}: Enter a number between 1 and 9:")
    input_location = int(input_location)
    while input_location not in range(1,10):
        print (f"Player {current_player}: Enter a number between 1 and 9:")
        input_location = int(input())
        continue
    
    #Inserting 'X' or 'O' into the desired location
    marker = player_details[1];
    ticTacToe.select_location_by_player(input_location, marker)
    count += 1
    
    # Check if one of the players won
    winner = ticTacToe.check_if_any_player_won(player_details[1], current_player)
    if count == 9 and not winner:
        print("It's a tie!")
        tie = True
        ticTacToe.print_tictactoeDisplayBoard()

    # Check if the players want to play TicTacToe again
    if winner or tie: #<-------  Game ends so program asks if any of them want to play again
        play = ticTacToe.play_again()
        if play:
            current_player = ''
            count = 0
