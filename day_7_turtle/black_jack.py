import random

def create_deck():
    deck = []
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for rank in range(2, 11):
            deck.append((rank, suit))
        for rank in ['J', 'Q', 'K', 'A']:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card, suit in hand:
        if isinstance(card, int):
            value += card
        elif card in ['J', 'Q', 'K']:
            value += 10
        else:  # Ace
            ace_count += 1
            value += 11
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(hand, name):
    print(f"{name}'s hand: ", end='')
    for card, suit in hand:
        print(f"{card} of {suit}", end=', ')
    print()

def main():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand(player_hand, "Player")
    display_hand(dealer_hand[:1], "Dealer")

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to [h]it or [s]tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand, "Player")
        else:
            break

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("Player busts! Dealer wins.")
        return

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_hand(dealer_hand, "Dealer")
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
