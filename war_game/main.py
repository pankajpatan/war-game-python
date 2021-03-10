import random
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self):
        print("crating new orderd deck")
        self.allcards = [(i, j) for i in SUITE for j in RANKS]

    def shuffle(self):
        print('shuffling deck')
        random.shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


print("lets start the game")

# creating new deck and spliting in half
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()


# creating Both of the player
comp = Player('computor', Hand(half1))
name = input("Enter Your Name")
user = Player(name, Hand(half2))


# set round count
total_rounds = 0
total_war = 0

# lets play

while(user.still_has_cards() and comp.still_has_cards()):
    total_rounds = total_rounds+1
    print("its time for a new round !")
    print("here are the current standings :")
    print(user.name + "count :" + str(len(user.hand.cards)))
    print(comp.name + "count :" + str(len(comp.hand.cards)))
    print("Both Player Play a card !")
    print("\n")

    # cards on the table represented by this list
    table_cards = []


# play cards
c_cards = comp.play_card()
p_cards = user.play_card()


# add to table cards
table_cards.append(c_cards)
table_cards.append(p_cards)

# check for war
# checking the rank of war
if c_cards[1] == p_cards[1]:
    total_war = total_war+1
    print("we have match! its time for war!")
    print("Each Player removes 3 cards 'face down' and then one card face up")
    table_cards.extend(user.remove_war_cards())
    table_cards.extend(comp.remove_war_cards())
    # play cards
    c_cards = comp.play_card()
    p_cards = user.play_card()

    # add to table cards
    table_cards.append(c_cards)
    table_cards.append(p_cards)

    #check to see who has higher rank
    if RANKS.index(c_cards[1])<RANKS.index(p_cards[1]):

        print(user.name+" has the higher card, adding to hand.")
        user.hand.add(table_cards)
    else:

        print(comp.name+" has the higher card, adding to hand.")
        comp.hand.add(table_cards)
else:
    #check to see who has higher rank
    if RANKS.index(c_cards[1])<RANKS.index(p_cards[1]):

        print(user.name+" has the higher card, adding to hand.")
        user.hand.add(table_cards)
    else:
       print(comp.name+" has the higher card, adding to hand.")
       comp.hand.add(table_cards)



print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")