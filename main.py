import random 



player_hit = random.randint(1, 8)
enemy_hit = random.randint(2, 9)
inventory = []
item_choice = ''

print('Welcome to Cyclops fighting simulator!\n')
response = input('would you like to fight the cyclops? [Y,N]  ').lower().strip()


def sword():
	print('\nyou got a sword.')
	inventory.append('sword')
def axe():
	print('\nyou got an axe.')
	inventory.append('axe')
def bow():
	print('\nyou got a bow.')
	inventory.append('bow')
def potato():
	print('\nyou got a potato.')
	inventory.append('potato')
def stick():
	print('\nyou got a stick.')
	inventory.append('stick')


def inventory_system(choice):
	choice = random.randint(1, 5)
	if choice == 1:
		sword()
	elif choice == 2:
		axe()
	elif choice == 3:
		bow()
	elif choice == 4:
		potato()
	elif choice == 5:
		stick()


def game_win():
	print('\n\n Y O U   W I N !')

def game_over():
	print('\n\n G A M E   O V E R.')



def left_path():
	global inventory

	print('\nyou decide to go left. after walking for a while, you spot a weapon lying on the side of the road!')

	inventory_system(item_choice)
	inventory.append(item_choice)

	if item_choice == 'sword':
		print('\n"`RUSTY SWORD`"\n increases your damage chance by 3.')
		print('\n\nyou now have a weapon to fight the cyclops.')
	elif item_choice == 'axe':
		print('\a"`AMAZING AXE`"\n increases your damage chance by 6! wow!')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'bow':
		print('\a"`TRUSTY BOW`"\n increases your damage chance by 2.')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'potato':
		print('\a"`GODLY POTATO`"\n increases your damage chance by 100. wtf?')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'stick':
		print('\a"`UNPLEASENT STICK`"\n decreases your damage chance by 1. oof.')
		print('you now have a weapon to fight the cyclops.')



def right_path():
	global inventory

	print('\nyou walk down the left path. soon after, you come across what you think might be a weapon...')

	inventory_system(item_choice)
	inventory.append(item_choice)

	if item_choice == 'sword':
		print('\n"`RUSTY SWORD`"\n increases your damage chance by 3.')
		print('\n\nyou now have a weapon to fight the cyclops.')
	elif item_choice == 'axe':
		print('\a"`AMAZING AXE`"\n increases your damage chance by 6! wow!')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'bow':
		print('\a"`TRUSTY BOW`"\n increases your damage chance by 2.')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'potato':
		print('\a"`GODLY POTATO`"\n increases your damage chance by 100. wtf?')
		print('you now have a weapon to fight the cyclops.')
	elif item_choice == 'stick':
		print('\a"`UNPLEASENT STICK`"\n decreases your damage chance by 1. oof.')
		print('you now have a weapon to fight the cyclops.')




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
			player_hit = random.randint(4, 12)
		elif inventory[0] == 'axe':
			player_hit = random.randint(7, 14)
		elif inventory[0] == 'bow':
			player_hit = random.randint(3, 11)
		elif inventory[0] == 'potato':
			player_hit = random.randint(101, 201)
		elif inventory[0] == 'stick':
			player_hit = random.randint(0, 10)
			
		enemy_hit = random.randint(4, 18)
		print('\nyou hit the cyclops for ' + str(player_hit) + ' damage!\n')
		print('the cyclops hits you for ' + str(enemy_hit) + ' damage!\n')

		if player_hit > enemy_hit:
			game_win()
		elif player_hit < enemy_hit:
			game_over()
	else:
		print('\nthe cyclops eats you alive.')





main_script()