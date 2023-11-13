import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han,
      
      In this traditional Japanese dice game, two dice are  roll in a bamboo
      cup by the dealer sitting on the floor.  The Player must guess if the
      dice total to an even (cho) or odd (han number.''')
    
purse = 5000
while True:  # Main game loop.
    # Place your get:
    print('You have', purse, 'mon. How much do you bet (or QUIT)')
    while True
