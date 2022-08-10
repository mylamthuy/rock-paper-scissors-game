while True:
    player1 = input('Player 1 name: ')
    player2 = input('Player 2 name: ')
    print('---Begin---')
    print('Hi', player1, ',')
    choice1 = int(input('What would you choose: 0: scissors; 1: rock; 2: paper\n'))
    if choice1 not in (0,1,2):
        choice1 = int(input("Let's choose again: 0: scissors; 1: rock; 2: paper\n"))
    print('Hi', player2, ',')
    choice2 = int(input('What would you choose: 0: scissors; 1: rock; 2: paper\n'))
    if choice2 not in (0,1,2):
        choice2 = int(input("Let's choose again: 0: scissors; 1: rock; 2: paper\n"))
    lst = ['scissors', 'rock', 'paper']
    print('   ', player1, 'chooses: ', lst[choice1])
    print('   ', player2, 'chooses: ', lst[choice2])
    print('--- *** Result *** ---')
    result = ''
    if choice1 == choice2:
        result = 'Draw'
    elif choice1 == 0:
        if choice2 == 1:
            result = player2 + ' win'
        else:
            result = player1 + ' win'
    elif choice1 == 1:
        if choice2 == 0:
            result = player1 + ' win'
        else:
            result = player2 + ' win'
    elif choice1 == 2:
        if choice2 == 0:
            result = player2 + ' win'
        else:
            result = player1 + ' win'
    print(result)
    
    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break