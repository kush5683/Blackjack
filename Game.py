import time
from colorama import init, Fore, Style
from Dealer import Dealer
from Player import Player

# Initialize colorama
init(autoreset=True)


class Game:
    def __init__(self, num_players: int = 1):
        self.num_players: int = num_players
        self.dealer: Dealer = Dealer()
        self.players: list[Player] = []
        self.minimal_bet: int = 10
        for _ in range(num_players):
            self.players.append(Player())

    def play_round(self):
        self.reset()
        # Deal two cards to each player
        for player in self.players:
            while player.bet < self.minimal_bet:
                get_bet: int = int(
                    input(f'Minimum bet {self.minimal_bet}\nYour bet: '))
                if get_bet < self.minimal_bet:
                    print('Bet is too low')
                    continue
                print(f"Remaining balance: {player.place_bet(get_bet)}")

            player.hit(self.dealer.deal())
            player.hit(self.dealer.deal())

        # Deal two cards to the dealer
        self.dealer.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal(hidden=True))

        # Player's turn
        for player in self.players:
            while player.hand_value < 21:
                print('Player hand:')
                for card in player.hand[:-1]:
                    print(card)
                    time.sleep(1)
                # Print the last card in green
                print(Fore.GREEN + str(player.hand[-1]) + Style.RESET_ALL)
                print('Dealer hand:')
                for card in self.dealer.hand:
                    print(card)
                    time.sleep(1)
                action: str = input('Do you want to hit or stay? ')
                if action == 'hit':
                    player.hit(self.dealer.deal())
                else:
                    break

        # Dealer's turn
        while self.dealer.hand_value < 17:
            self.dealer.hit(self.dealer.deal())

        # Display final hands
        print(f'Player hand: {player.hand_value}')
        print(f'Dealer hand: {self.dealer.hand_value}')
        print('Player hand:')
        for card in player.hand:
            print(card)
        print('Dealer hand:')
        for card in self.dealer.hand:
            print(card.reveal())

        # Determine the outcome
        if player.hand_value > 21:
            print('Player busts')
            player.balance -= player.bet
        elif self.dealer.hand_value > 21:
            print('Dealer busts')
        elif player.hand_value > self.dealer.hand_value:
            print('Player wins')
            player.balance += player.bet * 1.5
        elif player.hand_value < self.dealer.hand_value:
            print('Dealer wins')
        else:
            print('Push')

        print(f'Player balance: {player.balance}')
        if player.balance < self.minimal_bet:
            print('Game over. You are out of money')
            return
        play_again: str = input('Do you want to play again? ')
        if play_again == 'yes':
            self.play_round()

    def reset(self):
        self.dealer = Dealer()
        for player in self.players:
            player.hand = []
            player.hand_value = 0
            player.hand_soft = False
            player.bet = 0


if __name__ == '__main__':
    game = Game()
    game.play_round()
