'''
A card game of BlackJack written to practice the use of classes
'''
import random
import time
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades' ]
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2,'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1 }

class Card():
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck():
	def __init__(self):
		self.all_cards = []
		for rank in ranks:
			for suit in suits:
				self.all_cards.append(Card(suit, rank))

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()

class Player():
	

	def __init__(self,name,coins,points=0):
		self.name = name
		self.coins = coins
		self.all_cards = []
		self.points = points


	def bet(self,num):
		self.coins -= num

	def win(self,win):
		self.coins += win

	def add_card(self,card):
		self.all_cards.append(card)

	def clear_cards(self):
		self.all_cards = []

	def print_cards(self):	#printing all cards - designed for player purpose
		for card in self.all_cards:
			print(card)

	def print_one_card(self,counter): # for dealer
		print(self.all_cards[counter])

	def add_won(self,won):
		self.coins += won

	# def pts_count(self):
	# 	self.points = 0
	# 	for card in self.all_cards:
	# 		self.points += card.value
	# 	return self.points

	def pts_count(self):
		self.points = 0
		ace_bonus = False
		for card in self.all_cards:
			if card.rank == "Ace":
				ace_bonus = True
			self.points += card.value
		if ace_bonus and self.points < 12:
			#print("As liczony jako 11!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			self.points += 10 # only one Ace would be count as 11, not 1 :)
		return self.points

	def bet(self):
		print(self)
		bet = self.coins + 1
		while bet > self.coins:
			while True:
				try:
					bet = int(input("Please enter your bet: "))
				except:
					print("You must input number of coins you want to bet!")
				else:
					break	
		self.coins -= bet
		return bet

	def __str__(self):
		return self.name + " with: " + str(self.coins) + " coins."

def start_deal(deck_name,p_name, computer): # dealing 2 card for player and dealer
	p_name.clear_cards()
	computer.clear_cards()
	deck_name.shuffle()
	for number in [0,1]:
		p_name.add_card(deck_name.deal_one())
		computer.add_card(deck_name.deal_one())

def print_table(pl,comp):
	print("\n"*40)
	print("On table: \n")
	print(comp.name)
	comp.print_one_card(0) 
	print( '[X] \n\n')
	print(pl.name)
	pl.print_cards()




# Main game...
# Initalize:
init_coins = 10
bjdeck = Deck()

print("Welcome to the BLACKJACK GAME!")
name = input("Please, enter your name: ")
player1 = Player(name,init_coins)
dealer = Player('Dealer',init_coins)
game_on = True 



while game_on:
	play_again = ""
	start_deal(bjdeck,player1,dealer)
	bet = player1.bet()
	while True:
		player1.pts_count()
		if player1.points <22:
			print_table(player1,dealer)
			hit = 'd'
			while hit.upper() not in ['H', 'HIT', 'P', 'PASS']:
				hit = input('Hit or pass (H/P): ')
			if hit.upper() in ['H', 'HIT']:
				karta = bjdeck.deal_one()
				print(karta)
				player1.add_card(karta)
			else:
				print_table(player1,dealer)
				print(player1.name + " has " +str(player1.points) + " points.")
				print("\n\n")
				dealer.pts_count()
				dealer.print_cards()
				while dealer.points <21:
					if dealer.points > player1.points:
						print(f"Dealer has {dealer.points} points.")
						print("You lost the deal!")
						break
					elif dealer.points == 21:
						print("Deuce!")
						player1.win(bet)
						break
					else:
						time.sleep(3)
						dealer.add_card(bjdeck.deal_one())
						dealer.print_one_card(-1)
						dealer.pts_count()
				else:
					if dealer.points == 21:
						print(f"Dealer has {dealer.points} points.")
						print("You lost the deal!")
						break
					else:
						print(f"Dealer has {dealer.points} points.")
						print("\nYou won the deal!")
						player1.win(bet*2)

				break #pass cards
		else:
			print("You lost the deal!!")
			break
	if player1.coins == 0:
		print("You do not have any coins left. You LOST!")
		game_on = False
		break
	while play_again.upper() not in ['Y', 'YES', 'N', 'NO']:
		play_again = input("Would you like to play again? (Y/N): ")
		if play_again.upper() in ['Y','YES']:
			game_on = True
			play_again = ''
			break
		else:
			print("Thank you for playing!")
			game_on=False

		break
