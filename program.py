import random
user=input('Enter (r)for rock,(p) for paper,(s) for scissors:')
comp=random.choice(['r','p','s'])
print(f'computer chose:{comp}')
if user==comp:
    print("It's a Tie!!")
elif (user=='r' and comp=='s') or (user=='s'and comp=='p') or (user=='p' and comp=='r'):
    print('Yay! You Won.')
else:
    print('You Lost')