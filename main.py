import random 

player_hit = random.randint(1, 8)
enemy_hit = random.randint(2, 9)
inventory = []

print('Welcome to Cyclops fighting simulator!\n')
response = input('would you like to fight the cyclops? [Y,N]  ').lower().strip()

def game_win():
	print('\n\n Y O U   W I N !')

def game_over():
	print('\n\n G A M E   O V E R.')

def left_path():
	global inventory

	print('\nyou decide to go left. after walking for a while, you spot a sword lying on the side of the road!')
	print('\nyou pick up the sword.')

	inventory.append('sword')

	print('\n"`RUSTY SWORD`"\n increases your damage chance by 3.')
	print('\n\nyou now have a weapon to fight the cyclops.')

def right_path():
	global inventory

	print('\nyou walk down the left path. soon after, you come across what you think might be a weapon...')
	print('\nyou pick up the stick.')

	inventory.append('stick')

	print('\n"`UNPLEASENT STICK`"\n decreases your damage chance by 1')
	print('\nyou now have a weapon to fight the cyclops')

def main_script():
	global player_hit
	global enemy_hit
	global inventory
	global response

	if response == 'y':
		response = input('\nyou need a weapon to fight enemies. would you like to search for one? [Y,N]  ').lower().strip()

		if response == 'y':
			response = input('\nyou begin looking around when you spot a fork in the road. press 1 to go left, and press 2 to go right. [1,2]  ')

			if response == '1':
				left_path()
			elif response == '2':
				right_path()

		if inventory[0] == 'sword':
			player_hit = random.randint(3, 11)
		elif inventory[0] == 'stick':
			player_hit = random.randint(0, 7)
			
		enemy_hit = random.randint(2, 9)
		print('\nyou hit the cyclops for ' + str(player_hit) + ' damage!\n')
		print('the cyclops hits you for ' + str(enemy_hit) + ' damage!\n')

		if player_hit > enemy_hit:
			game_win()
		elif player_hit < enemy_hit:
			game_over()
	else:
		print('\nthe cyclops eats you alive.')


main_script()