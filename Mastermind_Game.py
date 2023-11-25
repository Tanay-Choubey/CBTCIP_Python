import random
def generate_number(n):
     x=''.join(random.choice('0123456789') for _ in range(n))
     return x
# game begins
n = 4  
print("Lets begin the Mastermind game by Tanay Choubey")
print(f"\nPlayer 1 will set a {n}-digit number in the mind, and Player 2 will guess.")
print("\n- denotes the digit/s doesn't exist only in the number")
print("X denotes the digit/s exist but not in correct position")
print("0 denotes the digit/s is in the correct position")
# Player 1 sets the secret number
s1 = generate_number(n)
a2 = 0
while True:
    # Player 2 makes a guess :
    g2 = input(f"\nPlayer 2, enter your {n}-digit guess: ")
    a2 += 1
    # player 2 guesses Correctly
    if g2 == s1:
        print("\nCongratulations, Player 2! You guessed the number {} correctly in {} attempts.".format(s1, a2))
        break
    # player 2 guesses the number wrong
    if len(s1) != len(g2):
        print(f'\nWrong Guess ! Please guess a {len(s1)}-digit number.')
    else:
        hint = ''
        for i in range(len(s1)):
            if s1[i] == g2[i]:
                hint += 'O' 
            elif g2[i] in s1:
                hint += 'X'  
            else:
                hint += '-'  
        print("Hint: {}".format(hint))
print("\nNow, Player 2 will set the number in the mind , and Player 1 will guess.")
# Player 2 sets the secret number
s2 = generate_number(n)
a1 = 0
while True:
    # Player 1 makes a guess
    g1 = input(f"\nPlayer 1, enter your {n}-digit guess: ")
    a1 += 1
    # Player 1 guesses the number correctly
    if g1 == s2:
        print("\nCongratulations, Player 1! You guessed the number {} correctly in {} attempts.".format(s2, a1))
        break
    if len(s2) != len(g1):
        print(f'\nInvalid guess length. Please guess a {len(s2)}-digit number.')
    else:
        hint = ''
        for i in range(len(s2)):
            if s2[i] == g1[i]:
                hint += 'O'  
            elif g1[i] in s2:
                hint += 'X'  
            else:
                hint += '-'  
        print("Hint: {}".format(hint))
# To decide who won the game at the end
if a1 < a2:
    print("\nPlayer 1 is crowned Mastermind! Guessed the number in fewer attempts.")
elif a1 > a2:
    print("\nPlayer 2 is crowned Mastermind! guessed the number in fewer attempts.")
else:
    print("\nIt's a tie! Both players guessed the number in the same number of attempts.")