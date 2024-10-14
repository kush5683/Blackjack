import time
from colorama import init, Fore, Style
from Dealer import Dealer
from Player import Player

# Initialize colorama
init(autoreset=True)

class Game:
    def __init__(self, num_players: int=1):
        self.num_players: int = num_players
        self.dealer: Dealer = Dealer()
        self.players: list[Player] = []
        for _ in range(num_players):
            self.players.append(Player())

    def play(self):
        # Deal two cards to each player
        for player in self.players:
            player.hit(self.dealer.deal())
            time.sleep(1)  # Delay to emulate dealing time
            player.hit(self.dealer.deal())
            time.sleep(1)  # Delay to emulate dealing time

        # Deal two cards to the dealer
        self.dealer.hit(self.dealer.deal())
        time.sleep(1)  # Delay to emulate dealing time
        self.dealer.hit(self.dealer.deal(hidden=True))
        time.sleep(1)  # Delay to emulate dealing time

        # Player's turn
        for player in self.players:
            while player.hand_value < 21:
                print('Player hand:')
                for card in player.hand[:-1]:
                    print(card)
                # Print the last card in green
                print(Fore.GREEN + str(player.hand[-1]) + Style.RESET_ALL)
                print('Dealer hand:')
                for card in self.dealer.hand:
                    print(card)
                action: str = input('Do you want to hit or stay? ')
                if action == 'hit':
                    player.hit(self.dealer.deal())
                    time.sleep(1)  # Delay to emulate dealing time
                else:
                    break
            if player.hand_value == 21:
                print('Blackjack!')
            elif player.hand_value > 21:
                print('Player busts')

        # Dealer's turn
        while self.dealer.hand_value < 17:
            self.dealer.hit(self.dealer.deal())
            time.sleep(1)  # Delay to emulate dealing time

        # Display final hands
        print(f'Player hand: {player.hand_value}')
        print(f'Dealer hand: {self.dealer.hand_value}')
        print('Player hand:')
        for card in player.hand:
            print(card)
        print('Dealer hand:')
        for card in self.dealer.hand:
            print(card)

        # Determine the outcome
        if player.hand_value > 21:
            print('Player busts')
        elif self.dealer.hand_value > 21:
            print('Dealer busts')
        elif player.hand_value > self.dealer.hand_value:
            print('Player wins')
        elif player.hand_value < self.dealer.hand_value:
            print('Dealer wins')
        else:
            print('Push')

if __name__ == '__main__':
    game = Game()
    game.play()
