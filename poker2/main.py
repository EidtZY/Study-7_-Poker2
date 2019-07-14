
from machine.std_mach import create_deck,\
                            shuffled_deck,\
                            record_deck
from dealer.mike import deal_to_a_player,deal_to_multi_players
# FIRST
# 新牌一副
first_deck = []
create_deck(first_deck)
record_deck(first_deck, 'deck-001.txt')
shuffled_deck(first_deck)
record_deck(first_deck, 'deck-002.txt')
# SECOND
'''
player1_deck = []
deal_to_a_player(first_deck, 10, player1_deck)
record_deck(player1_deck, 'player1_deck.txt')

player2_deck = []
deal_to_a_player(first_deck, 10, player2_deck)
record_deck(player2_deck, 'player2_deck.txt')

player3_deck = []
deal_to_a_player(first_deck, 10, player3_deck)
record_deck(player3_deck, 'player3_deck.txt')
'''
#THIRD
player1_deck = []
player2_deck = []
player3_deck = []
player4_deck = []
deal_to_multi_players(first_deck,player1_deck,player2_deck,player3_deck,player4_deck)
record_deck(player1_deck, 'player1_deck.txt')
record_deck(player2_deck, 'player2_deck.txt')
record_deck(player3_deck, 'player3_deck.txt')
record_deck(player4_deck, 'player4_deck.txt')
