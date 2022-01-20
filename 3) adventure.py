"""
Description:
This program first asks the user what adventure they'd like first (halloween or lottery).
It then progresses the plot based on their decisions, with some paths leading to a win, and others to a loss.
After the first 2, it gives 2 more adventures to choose from (prince or detective), which also continues in a similar way.

I've also learned some new tricks in Python like using goOn to start the game and hold variable data, use some formatting to decorate the win / lose screen, and time module to delay printed text

There are a total of 4 storylines in this game:
1. Halloween
2. Lottery
3. Prince
4. Detective
"""
# The time module give a nice delayed effect to the printed text
import time

# Variable that decides whether the game will run again or not.
goOn = True

# Variables that store how many wins and loses you get.
wins = 0
loses = 0

# Displays a message when you win!
def win():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Congratulations, you actually won! You have finished this adventure.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Displays a message when you lose...
def lose():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Dang, you lost! Game over.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))

# Return T or F for Y or N (to be used to reassign goOn var).
def cont(yn):
    if yn == 'y':
        return True
    elif yn == 'n':
        return False


# Main program. runs the Choose Your Own Adventure game.

while goOn == True:

    print("Welcome! Please choose your first adventure... ")
    time.sleep(1)
    print("You are a 10 year-old trick or treater on the eve of Halloween... OR You've just won a $10 million lottery and are deciding where to spend your fortune...")
    # Decide between halloween or lottery.
    choice = input('Which adventure do you choose? (halloween / lottery) ').lower()

    if choice == 'halloween':

        print("Good choice! As you and your friends set off into the evening, you see a huge mansion and a withered house, both with decorations and lights on.")
        time.sleep(1)
        # Decide between mansion or house.
        choice = input('Do you go to the mansion or house? (mansion / house) ').lower()

        if choice == 'mansion':
            print("You walk past the steel gates and oak trees and onto the main stoop. After ringing the bell, a nice couple gives you a bag of expensive candy. You turn back, only to see a group of teenagers who want your candy!")
            time.sleep(1)
            # Decide between fight and run away
            choice = input('Do you fight them, or run away? (fight / run) ').lower()
            
            if choice == 'fight':
                print('{}'.format("Your big brother charges into them and actually scares them away. You and your friends walk back home with all your candy!"))
                time.sleep(3)
                win()
                wins += 1

            elif choice == 'run':
                print('Oh no! You make a dash for a hiding place, but you cannot find one in the open courtyard! The teenagers swipe all your candy...')
                time.sleep(1)
                print('You and your friends are defeated, empty-handed and hungry.')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')

        if choice == 'house':
            print("You and your friends walk past the driveway and grass, but you suddenly notice a figure staring at you from the window!")
            time.sleep(1)
            # Decide between ahead and turn back
            choice = input('Do you go ahead, or turn back? (ahead / back) ').lower()
            
            if choice == 'ahead':
                print("You push your nervous friends to trudge along and you step onto the porch. After ringing the doorbell, a nice old lady with a charming smile gives you a bag of expensive candy. She tells you, 'Enjoy your treats kids! Have a nice evening!'.")
                time.sleep(1)
                print("You head back home with a truckload of nice sweets!")
                win()
                wins += 1

            elif choice == 'back':
                print('You swiftly walk away from the spooky house, only to see a dozen other kids running towards you! Stuck between a rock and a hard place, they take all your candy away...')
                time.sleep(1)
                print('You and your friends are defeated, empty-handed and hungry.')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')
                
    elif choice == 'lottery':

        print("Overjoyed with your big win, your friends tell you to buy a mega-mansion in Los Angeles, but your parents tell you to invest it all in the stock market...")
        time.sleep(1)
        # Decide between mansion and stocks
        choice = input('Do you buy the mega-mansion, or invest it all in stocks? (mansion / stocks) ').lower()

        if choice == 'mansion':
            print("You bought a $9 million mansion off the coast of Los Angeles, but you only have $1 million left! Your neighbor recommends to grow the remaing money by trading, but your friends say don't sweat it...")
            time.sleep(1)
            # Decide between trading and leaving it be
            choice = input('Do you learn trading, or leave your money be? (trading / leave it) ').lower()
            
            if choice == 'trading':
                print("You learn trading and grow your money into $100 million after a few years. With your friends in shock, you can now have a blast of a time with all your money!")
                time.sleep(1)
                print("With $100 million in hand, the world is yours to buy...")
                win()
                wins += 1
            elif choice == 'leave it':
                print('Unfortunately, your money depletes like a drying riverbed, and after a year you cannot even afford to pay your mega-mansion electricty bill...')
                time.sleep(1)
                print('Bankrupt, you return to your old life...')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')

        if choice == 'stocks':
            print("Asking your parents for advice, your Dad says invest in big, stable companies like Funky and Contech, but your Mom says go for small start-ups with big potential...")
            time.sleep(1)
            # Decide between small and big companies
            choice = input('Do you invest in the big companies, or the small ones? (big / small) ').lower()
            
            if choice == 'small':
                print("You put your remaining fortune into the small startups, only for them to have a remarkable year! Your outcome is a $20 million profit")
                time.sleep(1)
                print("Having doubled your lottery win, you safely go home to splurge to your heart's content...")
                time.sleep(1)
                win()
                wins += 1

            elif choice == 'big':
                print('You put your remaining fortune into the big companies, only for them to have a bad year! Your outcome is a $2 million debt...')
                time.sleep(1)
                print("With your Dad blamefree, you are back to your old life with a debt of $2 million. How will you pay your mansion bills now, eh? ")
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')
    
    else:
        print('Please pick halloween or lottery next time!')

    print("Welcome back! Please choose your second adventure... ")
    time.sleep(1)
    print("You are a prince in the Mushroom Kingdom, hoping to free your beloved princess from the dreaded Bowser... OR You are a detective investigating clues to catch an Italian mafia boss...")
    # Decide between prince or detective.
    choice = input('Which character do you choose? (prince / detective) ').lower()

    if choice == 'prince':

        print("You are at Bowser's castle where the princess is held, but you need a weapon to fight Bowser! What weapon do you choose?")
        time.sleep(1)
        # Decide between flamethrower and sword.
        choice = input('Do you choose a flamethrower, or a sword? (flame / sword) ').lower()

        if choice == 'flame':
            print("Great choice! The duel is quick but decisive! Do you choose to open fire and end Bowser, or distract him to buy you time?")
            time.sleep(1)
            # Decide between instant fire and distraction
            choice = input('Do you open fire, or distract him? (fire / distract) ').lower()
            
            if choice == 'distract':
                print("You distract bowser with a climatic chit-chat, then when he's too into it, you burst open your flamethrower onto him!")
                time.sleep(3)
                print("He burns to a fiery crisp, releasing the princess from her eternal cage...")
                print("She returns to you like a falling flower, and you headback home with your beloved princess...")
                win()
                wins += 1

            elif choice == 'fire':
                print('You open full fire towards Bowser, but he is just too quick! He jumps and lands behind you, dealing one good blow to your abdomen...')
                time.sleep(1)
                print('Unfortunately, you, the fabled hero, could not survive the injury, leaving the princess to Bowser forever...')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')

        if choice == 'sword':
            print("Great choice! The duel is a quick but decisive one! Do you choose to face him sword to sword, or run away?")
            time.sleep(1)
            # Decide between facing him or running away
            choice = input('Do you choose to face him, or run away? (face him / run) ').lower()
            
            if choice == 'run':
                print("You run away to his surprise, but make a wall jump and land behind him! With one good cut to his abdomen, he is falls to the ground, releasing the princess from her eternal cage...")
                time.sleep(3)
                print("She returns to you like a falling flower, and you headback home with your beloved princess...")
                win()
                wins += 1

            elif choice == 'face him':
                print('You make your move and clash swords with Bowser, but you forget that he is 3 times stronger than you! He easily overpowers you and makes you fall to the ground...')
                time.sleep(1)
                print('Unfortunately, you, the fabled hero, could not survive the injury, leaving the princess to Bowser forever...')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')
                
    elif choice == 'detective':

        print("You arrive at the crime scene, only to find 2 clues that lead any further: a diaper, and a ring...")
        time.sleep(1)
        # Decide between diaper and ring
        choice = input('Which item do choose to investigate? (diaper / ring) ').lower()

        if choice == 'diaper':
            print("Good choice, I guess? The diaper contains DNA evidence of the Mafia boss, and you trace him to an outdoor picnic. However, you don't know what he looks like, but you do know his car...")
            time.sleep(1)
            # Decide between calling him or waiting it out
            choice = input('To find him, do you call his number to get him to run, or do wait till he gets in his car? (call / wait) ').lower()
            
            if choice == 'call':
                print("After having heard his number ring, you identify him in the crowd! He makes a run for it, but with the place surrounded, he is caught within minutes...")
                time.sleep(3)
                print("Another case solved, and another promotion to senior detective! Well played!")
                win()
                wins += 1
            elif choice == 'wait':
                print('You wait till the picnic is over, only to find that the Mafia boss used a Taxi to getaway! Looking at his abandoned car in the parking lot, you dwell upon your mistakes...')
                time.sleep(1)
                print('With the Mafia boss on the loose again, you have been demoted to junior detective whilst dozens of people remain missing...')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')

        if choice == 'ring':
            print("Good choice! The ring was found to have the Mafia boss's fingerprint on it. It leads you to his apartment, but how exactly do you arrest him?")
            time.sleep(1)
            # Decide between barging in or waiting it out
            choice = input('Do you barge in with officers, or wait till he comes out unknowingly? (barge / wait) ').lower()
            
            if choice == 'barge':
                print("You barge into his apartment and find him in the living room bewildered... After having put him in handcuffs, he is off to the police station...")
                time.sleep(3)
                print("Another case solved, and another promotion to senior detective! Well played!")
                win()
                wins += 1

            elif choice == 'wait':
                print('You and your officers wait outside the building, only for the Mafia boss to notice! He makes a secret getaway under your noses...')
                time.sleep(1)
                print('With the Mafia boss on the loose again, you have been demoted to junior detective whilst dozens of people remain missing...')
                time.sleep(1)
                lose()
                loses += 1

            else:
                    print('Please pick a valid input!')
    
    else:
        print('Please pick prince or detective next time!')

    time.sleep(3)
    print('You have won {} times.'.format(wins))
    print('You have lost {} times.'.format(loses))
    time.sleep(2)
    decision = input('Do you want to play again? y/n \n')
    goOn = cont(decision)
