import random

while True:
    player = input('Player name: ')
    print('---Begin---')
    print('Hey', player,',')
    choice1 = int(input('What would you choose: 0: scissors; 1: rock; 2: paper\n'))
    if choice1 not in (0,1,2):
        choice1 = int(input("Let's choose again: 0: scissors; 1: rock; 2: paper\n"))
    choice2 = random.randint(0,2)
    lst = ['scissors', 'rock', 'paper']
    print('')
    print('   ', player, 'chooses: ', lst[choice1])
    print('   AI chooses: ', lst[choice2])
    print('--- *** Result *** ---')
    result = ''
    if choice1 == choice2:
        result = 'Draw'
    elif choice1 == 0:
        if choice2 == 1:
            result = 'AI win'
        else:
            result = player + ' win'
    elif choice1 == 1:
        if choice2 == 0:
            result = player + ' win'
        else:
            result = 'AI win'
    elif choice1 == 2:
        if choice2 == 0:
            result = 'AI win'
        else:
            result = player + ' win'
    print(result)
    
    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break