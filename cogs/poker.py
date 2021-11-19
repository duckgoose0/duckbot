import discord
import os
import random
import re
from discord.ext import commands

def winCondition(checkVal = [0, 0, 0, 0, 0], checkSuit = [0, 0, 0, 0, 0]):
	x = [0, 0]

	valSort = checkVal
	suitSort = checkSuit

	valSort.sort()
	suitSort.sort()
	
	pair = 0
	three = False
	four = False
	straight = False
	flush = False

	#flush check
	if(suitSort[0] == suitSort[1] == suitSort[2] == suitSort[3] == suitSort[4]):
		flush = True
	else:
		pass
	
	#straight check
	kingCheck = False
	if(valSort[0] == 1 and valSort[4] == 13):
		kingCheck = True
		valSort[0] == 14
		valSort.sort()

	if(valSort[0] + 4 == valSort[1] + 3 == valSort[2] + 2 == valSort[3] + 1 == valSort[4]):
		straight = True
		if(kingCheck):
			valSort[4] = 1
		valSort.sort()
	else: 
		pass

	#four of a kind check
	fourIndex = 0
	for n in range(1):
		if(valSort[n] == valSort[n+1] == valSort[n+2] == valSort[n+3]):
			four = True
			fourIndex = n + 3

	#three of a kind check
	threeIndex = 0
	for n in range(2):
		if(valSort[n] == valSort[n+1] == valSort[n+2]):
			three = True
			threeIndex = n + 2

	#pair check
	pairIndex = 0
	updater = 0
	for n in range(4):
		if(updater % 2 != 0):
			updater += 1
		elif(valSort[n] == valSort[n+1]):
			pair += 1
			pairIndex = n + 1
			updater += 1
		else:
			pass

	if(straight and flush):
		x[0] = 8
		x[1] = valSort[4]
	elif(four):
		x[0] = 7
		x[1] = fourIndex
	elif(pair == 1 and three):
		x[0] = 6
		x[1] = valSort[threeIndex]
	elif(flush and not straight):
		x[0] = 5
		x[1] = valSort[4]
	elif(straight and not flush):
		x[0] = 4
		x[1] = valSort[4]
	elif(three and pair == 0):
		x[0] = 3
		x[1] = valSort[threeIndex]
	elif(pair == 2):
		x[0] = 2
		x[1] = valSort[pairIndex] 
	elif(pair == 1):
		x[0] = 1
		x[1] = valSort[pairIndex] 
	else:
		x[0] = 0
		x[1] = valSort[4]

	return x 

class Poker(commands.Cog):

	def __init__(self, client):
		self.client = client

	global userCardID
	global userSuitID
	global botCardID
	global botSuitID
	global handConv

	userCardID = [0, 0, 0, 0, 0]
	userSuitID = [0, 0, 0, 0, 0]
	botSuitID = [0, 0, 0, 0, 0]
	botCardID = [0, 0, 0, 0, 0]
	handConv = [None, 'A:spades:', 'A:clubs:', 'A:hearts:', 'A:diamonds:', '2:spades:', '2:clubs:', '2:hearts:', '2:diamonds:', '3:spades:', '3:clubs:', '3:hearts:', '3:diamonds:', '4:spades:', '4:clubs:', '4:hearts:', '4:diamonds:', '5:spades:', '5:clubs:', '5:hearts:', '5:diamonds:', '6:spades:', '6:clubs:', '6:hearts:', '6:diamonds:', '7:spades:', '7:clubs:', '7:hearts:', '7:diamonds:', '8:spades:', '8:clubs:', '8:hearts:', '8:diamonds:', '9:spades:', '9:clubs:', '9:hearts:', '9:diamonds:', '10:spades:', '10:clubs:', '10:hearts:', '10:diamonds:', 'J:spades:', 'J:clubs:', 'J:hearts:', 'J:diamonds:', 'Q:spades:', 'Q:clubs:', 'Q:hearts:', 'Q:diamonds:', 'K:spades:', 'K:clubs:', 'K:hearts:', 'K:diamonds:']
	# 0 is set as an index to mean there is currently no card

	

	@commands.group(invoke_without_command = True)
	async def poker(self, ctx):
		await ctx.send('Welcome to Five-Card Poker! To start a new game, type `>>poker deal`. \n\nTo read the rules, type `>>poker rules`, or type ``>>poker rank`` to see a guide of the card rankings.')
		print('poker works')

	@poker.command()
	async def deal(self, ctx):
		userRef = [0, 0, 0, 0, 0]
		botRef = [0, 0, 0, 0, 0]

		for x in range(len(userCardID)):
			isSameCard = True
			while(isSameCard):
				userCardID[x] = random.randint(1, 13)
				userSuitID[x] = random.randint(0, 3)
				for i in range(len(userCardID)):
					if i == x:
						pass
					elif(int(userCardID[x]) == int(userCardID[i]) and int(userSuitID[x] == int(userSuitID[i]))):
						isSameCard = True
						print('randint error 0')
						break
					else:
						isSameCard = False

				for i in range(len(botCardID)):
					if(isSameCard):
						break
					elif(int(userCardID[x]) == int(botCardID[i]) and int(userSuitID[x] == int(botSuitID[i]))):
						isSameCard = True
						print('randint error 1')
						break
					else:
						isSameCard = False

		for x in range(len(botCardID)):
			isSameCard = True
			while(isSameCard):
				botCardID[x] = random.randint(1, 13)
				botSuitID[x] = random.randint(0, 3)
				for i in range(len(botCardID)):
					if i == x:
						pass
					elif(int(botCardID[x]) == int(botCardID[i]) and int(botSuitID[x] == int(botSuitID[i]))):
						isSameCard = True
						print('randint error 0')
						break
					else:
						isSameCard = False

				for i in range(len(userCardID)):
					if(isSameCard):
						break
					elif(int(botCardID[x]) == int(userCardID[i]) and int(botSuitID[x] == int(userSuitID[i]))):
						isSameCard = True
						print('randint error 1')
						break
					else:
						isSameCard = False

		for i in range(len(userCardID)):
			userRef[i] = 4 * userCardID[i] - userSuitID[i]
			botRef[i] = 4 * botCardID[i] - botSuitID[i]

		for i in range(len(userRef)):
			userRef[i] = handConv[int(userRef[i])]
			botRef[i] = handConv[int(botRef[i])]
						
		await ctx.send(f'Your cards are {userRef}.')
		print(userCardID)
		print(userSuitID)
		print(botCardID)
		print(botSuitID)

	@poker.command()
	async def discard(self, ctx, *args):
		userRef = [0, 0, 0, 0, 0]
		botRef = [0, 0, 0, 0, 0]
		userVal = 0
		botVal = 0
		userWin = False
		botWin = False
		tie = False

		remove = re.findall('\d', str(args))
		if(len(remove) == 0):
			print('no modification')
		else:
			for x in remove:
				if(int(x) > 5 or int(x) < 1):
					print('out of bounds')
				else:
					isUsedCard = True
					while(isUsedCard):
						userCardID[int(x) - 1] = random.randint(1, 13)
						userSuitID[int(x) - 1] = random.randint(0, 3)

						for i in range(len(userCardID)):
							if i == (int(x) - 1):
								pass
							elif(int(userCardID[int(x) - 1]) == int(userCardID[i]) and int(userSuitID[int(x) - 1] == int(userSuitID[i]))):
								print('randint error 2')
								break
							else:
								isUsedCard = False

						for i in range(len(botCardID)):
							if(isUsedCard):
								break
							elif(int(userCardID[int(x) - 1]) == int(botCardID[i]) and int(userSuitID[int(x) - 1] == int(botSuitID[i]))):
								print('randint error 3')
								break
							else:
								isUsedCard = False
					print('in bounds')

		for i in range(len(userCardID)):
			userRef[i] = 4 * userCardID[i] - userSuitID[i]

		for i in range(len(botCardID)):
			botRef[i] = 4 * botCardID[i] - botSuitID[i]

		for i in range(len(userRef)):
			userRef[i] = handConv[int(userRef[i])]
			botRef[i] = handConv[int(botRef[i])]
			
		userVal = winCondition(userCardID, userSuitID)
		botVal = winCondition(botCardID, botSuitID)

		if(userVal[0] > botVal[0]):
			userWin = True
		elif(botVal[0] > userVal[0]):
			botWin = True
		elif(userVal[0] == botVal[0]):
			if(userVal[1] > botVal[1]):
				userWin = True
			elif(userVal[1] < botVal[1]):
				botWin = True
			else:
				tie = True
		
		await ctx.send(f'After discarding cards, your hand is now {userRef}.')
		await ctx.send(f'My hand is {botRef}.')
		
		if(userWin):
			await ctx.send('You win, human! Great job!')
			print('user wins')
		elif(botWin):
			await ctx.send('I win this time, human! Better luck next time!')
			print('bot wins')
		elif(tie):
			await ctx.send('It\'s a tie!')
			print('its a tie lmao')
		else:
			raise Exception('There was an error: winner cannot be determined.')

		print(remove)
		print(userCardID)
		print(userSuitID)
		print(botCardID)
		print(botSuitID)

	@poker.command()
	async def rules(self, ctx):
		await ctx.send('''The game is simple! Follow **these** steps to play five-card poker with duckbot:
		
(1) Send `>>poker deal` to start a new game.
(2) Duckbot will show you your hand. Send `>>poker discard` followed by the cards you wish to discard, numbered 1-5 from left to right. To discard multiple cards, type the numbers separated by spaces (eg. `>>poker discard 2 4 5`). To keep your current hand, do not type anything after `>>poker discard`. This command ignores numbers below 1 and above 5.
(3) Duckbot will then show you your final hand, as well as its hand. It will finally show you who won, and the hands you formed!
		
Have fun!''')

	@poker.command()
	async def rank(self, ctx):
		await ctx.send('''There are ten playable hands in poker, with increasing value.
		
**1: Royal Flush.** A hand with A, K, Q, J, 10, all in the same suit. 
[A:hearts: K:hearts: Q:hearts: J:hearts: 10:hearts:]
**2: Straight Flush.** A hand with five consecutive cards in the same suit. 
[3:diamonds: 4:diamonds: 5:diamonds: 6:diamonds: 7:diamonds:]
**3: Four of A Kind.** A hand with four cards of the same value. 
[6:diamonds: 6:hearts: 6:spades: 6:clubs: 2:hearts:]
**4: Full House.** A hand with three cards of the same value alongside a separate pair. 
[4:hearts: 4:spades: 4:clubs: K:diamonds: K:spades:]
**5: Flush.** A hand with five cards of the same suit. 
[3:diamonds: 6:diamonds: K:diamonds: 10:diamonds: A:diamonds:]
**6: Straight.** A hand with five cards of consecutively increasing value. 
[7:hearts: 8:spades: 9:spades: 10:hearts: J:diamonds:]
**7: Three of A Kind.** A hand with three cards of the same value, with no other pair. 
[Q:spades: Q:hearts: Q:diamonds: A:diamonds: 6:clubs:]
**8: Two Pairs.** A hand with two pairs of cards of equal value. 
[2:clubs: 2:hearts: 5:spades: 5:hearts: 4:diamonds:]
**9: One Pair.** A hand with only one pair of equal-value cards. 
[8:hearts: 8:diamonds: J:diamonds: K:spades: A:spades:]
**10: High Card.** If none of the combinations above apply, the highest value card is played.

**Card Value:** A-2-3-4-5-6-7-8-9-10-J-Q-K-A''')

def setup(client):
	client.add_cog(Poker(client))