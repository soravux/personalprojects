import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.')
done = False
miles = 0
thirst = 0
tiredness = 0
distance = -20
drinks = 20

while not done:
    milestraveled = 0
    print()
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')

    user_choice = input('Your choice? ')
    print()

    if user_choice.upper() == 'Q':
        done = True
        break

    elif user_choice.upper() == 'E':
        print('Miles traveled:', miles)
        print('Drinks in canteen:', drinks)
        print('The natives are {0} miles behind you.'.format(miles-distance))

    elif user_choice.upper() == 'D':
        tiredness = 0
        print('The camel is happy.')
        distance += random.randrange(7, 15)

    elif user_choice.upper() == 'C':
        milestraveled = random.randrange(10, 21)
        miles += milestraveled
        print('You traveled {0} miles.'.format(milestraveled))
        thirst += 1
        tiredness += random.randrange(1, 4)
        distance += random.randrange(7, 15)

    elif user_choice.upper() == 'B':
        milestraveled = random.randrange(5, 13)
        miles += milestraveled
        print('You traveled {0} miles.'.format(milestraveled))
        thirst += 1
        tiredness += random.randrange(1, 2)
        distance += random.randrange(7, 15)

    elif user_choice.upper() == 'A':
        if drinks > 0:
            drinks -= 1
            print('You drink from your canteen.')
            thirst = 0
        else:
            print('You have no drinks remaining!')

    if random.randrange(20) == 1 and milestraveled:
        print('You found an oasis!')
        drinks = 20
        thirst = 0
        tiredness = 0

    if thirst > 6:
        print('You died of thirst')
        done = True
        break

    elif thirst > 4:
        print('You are thirsty')

    if tiredness > 8:
        print('Your camel is dead')
        done = True
        break

    elif tiredness > 5:
        print('Your camel is getting tired')

    if miles <= distance:
        print('You got caught by the natives')
        done = True
        break

    elif miles-distance < 15:
        print('The natives are getting close!')

    if miles >= 200:
        print('You traveled through the desert, you win!')
        done = True
        break
