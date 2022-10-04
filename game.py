from player import Player
from card import Card
def main():

    player1 = Player()

    while player1.score > 0:
        if player1.score > 0:
            card1 = Card()
            card2 = Card()
            print(f'The card is {card1.card}.')

            choice_loop = False
            while choice_loop == False:
                if choice_loop == False:
                    choice = input('Higher or lower? [h/l] ')
                    if choice.lower() == 'h':
                        output = card2.card > card1.card
                        choice_loop = True
                    elif choice.lower() == 'l':
                        output = card2.card < card1.card
                        choice_loop = True
                    else:
                        print('That is not a valid input.')

            if output == True:
                player1.score += 100
                print('You were right!')
            elif output == False:
                player1.score -= 75
                print('You were wrong!')

            print(f'Next card was: {card2.card}')
            print(f'Your score is: {player1.score}')

            play_again_loop = False
            while play_again_loop == False:
                if play_again_loop == False:
                    play_again = input('Play again? [y/n]')
                    if play_again.lower() == 'y':
                        play_again_loop = True
                    elif play_again.lower() == 'n':
                        play_again_loop = True
                        player1.score = 0
                    else:
                        print('That is not a valid input.')

if __name__ == '__main__':
    main()