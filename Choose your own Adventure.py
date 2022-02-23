name = input('Type in your name: ')
print('welcome', name, 'to this adventure!')

answer = input(
    'You are on a dirt road, it has come to an end and you can left or right. Which way would you like to go?: ').lower()

if answer == 'left':
    answer = input('You came to a river, you can walk around it or swim across? write walk to walk across or write swim to swim across: ')
    
    if answer == 'swim':
     print('You swam across the river and got eaten by an alligator')
    elif answer == 'walk':
        print('You ran for many miles and ran out of food and water causing you to die!')
    else:
        print('Not a valid option. You lose.')
        
elif answer == 'right':
    answer = input('You find a bridge that looks wobbly . DO you want to cross or go back. Write back to go back , or write cross to crosss it: ')

    if answer == 'back':
        print('You go back and lose!')
    elif answer == 'cross':
        input('You find a stranger . Do you want to talk to him (Yes/No): ').lower()

         if answer == "yes":
            print("You talked to the stranger, He turns out to be the Creator, he gives you GOLD and you win")
         
        elif answer == "no":
             print("You didn't talk to the Creator/Stranger . He felt that you are rude and he killed you! You Lose!")
        
        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

    

   
    
    
