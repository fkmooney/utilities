### exec(open("C:/Users/Kempton Mooney/Documents/Python_Scripts/adventure.py").read())

import random


#Preset Values
player_pos = [0,0]
nav = {'nx':0,'ny':1,'ex':1,'ey':0,'sx':0,'sy':-1,'wx':-1,'wy':0}
rooms = {'your steps feel like tremors, you start to feel dizzy and knock it off.':[0,0],
	'are tired by your efforts and lay down to sleep it off. \nYou wake up refreshed but with cottonmouthed.':[1,0],
	'have found an aspirin. Hurray!':[1,1],
	'find walking difficult, but no one said life is easy.':[0,1],
	'Youre getting good at this wlaking thing. \nDont let it go to your head.':[-1,1],
	'You are on a roll now! If only you had some bacon, some eggs, and some cheese.':[-2,1]}
print_pos = [[-2,1],[-1,1],[0,1],[1,1],[0,0],[1,0]]
goals_reached = [0,0]
goalxy = list(rooms.values())[random.randrange(0,6)]
while goalxy == [0,0]:
	goalxy = list(rooms.values())[random.randrange(0,6)]

# Proccesing
def walk():
	user_input = input('What do you want to do? Walk N, S, E, or W?')

	if user_input.lower() == 'n' or user_input.lower() == 'e' or user_input.lower() == 's' or user_input.lower() == 'w':
		player_pos[0] += nav['{}x'.format(user_input.lower())]
		player_pos[1] += nav['{}y'.format(user_input.lower())]
		
		try:
			check_pos_validity = list(rooms.keys())[list(rooms.values()).index(player_pos)]
			print('\nProgress! You {}'.format(check_pos_validity))
		except:
			print('\nOuch! You ran into a wall!')
			print('Maybe you should rethink if you are ready for this kind of thing.')
			player_pos[0] -= nav['{}x'.format(user_input.lower())]
			player_pos[1] -= nav['{}y'.format(user_input.lower())]
	else:
		print('\nI dont think thats a direction.. use N for north, E for east, S for south, W for west')
	
	if player_pos == goalxy and goals_reached[0] == 0:
		goals_reached[0] = 1
		print('Whoa, holy crap! \nYou realize this isnt even your house! Lets get the fuck out of here!')
	if player_pos == [0,0] and goals_reached[0] == 1:
		goals_reached[1] = 1
		print('That was close, you were able to escape before being found!')
		print('You make it to the street and see a deli.')
		print('Of course, you enter. The question is what do you order?')

# Starting Message
print('You wake up on the floor. It must have been a long night last night!\n')
ps = [' ',' ',' ',' ',' ',' ']


# Start
while not goals_reached == [1,1]:
	walk()
	ps = [' ',' ',' ',' ',' ',' ']

############################### END OF SCENE ONE #############################

player_pos = [0,0]
nav = {'coffeex':0,'coffeey':1,'bagelx':1,'bagely':0,'waterx':0,'watery':-1,'the specialx':-1,'the specialy':0}
rooms = {'Oh, thatll hit the spot! But you want something more.':[0,0],
	'Good call. Anything else?':[1,0],'And some aspirin as well. And?':[1,1],
	'Im not sure the person behind\n the counter understood you. \nMaybe try something else?':[0,1],
	'Youre getting good at this ordering thing. \nDont let it go to your head.':[-1,1],
	'You are on a roll now! \nIf only you had some bacon, some eggs, and some cheese.':[-2,1]}
print_pos = [[-2,1],[-1,1],[0,1],[1,1],[0,0],[1,0]]
goals_reached = [0,0]
goalxy = list(rooms.values())[random.randrange(0,6)]
while goalxy == [0,0]:
	goalxy = list(rooms.values())[random.randrange(0,6)]

# Proccesing
def walk():
	global player_pos
	user_input = input('What do you want to order: coffee, bagel, water, or the special?')

	if user_input.lower() == 'coffee' or user_input.lower() == 'bagel' or user_input.lower() == 'water' or user_input.lower() == 'the special':
		player_pos[0] += nav['{}x'.format(user_input.lower())]
		player_pos[1] += nav['{}y'.format(user_input.lower())]
		
		try:
			check_pos_validity = list(rooms.keys())[list(rooms.values()).index(player_pos)]
			print('\n{}'.format(check_pos_validity))
		except:
			print('\nWhoops, someone breaks in front of you and orders. \nYou have to be fast in this city!')
			print('Alright, champ, lets give this another try.\n What will it be?')
			player_pos[0] -= nav['{}x'.format(user_input.lower())]
			player_pos[1] -= nav['{}y'.format(user_input.lower())]
	else:
		print('\nThe person behind the counter didnt catch that. \nYou may have slurred your speeach.')
		print('You really ned to get something in you.\n What will it be?')
	
	if player_pos == goalxy and goals_reached[0] == 0:
		goals_reached[0] = 1
		print('Your bloodshot eyes are finally focusing. Good work!\nYou may live another day...')
		player_pos = [0,0]
	if player_pos == [0,0] and goals_reached[0] == 1:
		goals_reached[1] = 1
		print('Alright, refueled!\n Now you are ready to take on the world.')

# Starting Message
print('If only they would turn down the lights just a little bit, like to off.\n')
ps = [' ',' ',' ',' ',' ',' ']


# Start
while not goals_reached == [1,1]:
	walk()
	ps = [' ',' ',' ',' ',' ',' ']


############################### END OF SCENE TWO #############################

player_pos = [0,0]
nav = {'uptownx':0,'uptowny':1,'downtownx':1,'downtowny':0,'eastx':0,'easty':-1,'westx':-1,'westy':0}
rooms = {'Whoa!!! Too much foot traffic!\nYou are carried backwards, you weak salmon.':[0,0],
	'You pass an interesting store.':[1,0],
	'You stop and watch the good people ride \ntheir stationary bikes at the gym.':[1,1],
	'Nope, that is just the wrong answer.':[0,1],
	'Youre getting good at this walking thing. \nHeard that before?':[-1,1],
	'You try but it is too much work.\n You stopand are trampled by fellow pedestrians.\nYou pick yourself up.\nYou brush off the taste of concrete. \nYou look sternly ahead and hesitate.':[-2,1]}
print_pos = [[-2,1],[-1,1],[0,1],[1,1],[0,0],[1,0]]
goals_reached = [0,0]
goalxy = list(rooms.values())[random.randrange(0,6)]
while goalxy == [0,0]:
	goalxy = list(rooms.values())[random.randrange(0,6)]

# Proccesing
def walk():
	global player_pos
	user_input = input('What next?: uptown, downtown, east, or west?')

	if user_input.lower() == 'uptown' or user_input.lower() == 'east' or user_input.lower() == 'downtown' or user_input.lower() == 'west':
		player_pos[0] += nav['{}x'.format(user_input.lower())]
		player_pos[1] += nav['{}y'.format(user_input.lower())]
		
		try:
			check_pos_validity = list(rooms.keys())[list(rooms.values()).index(player_pos)]
			print('\n{}'.format(check_pos_validity))
		except:
			print('Come on, you can do better than that! \nAlright, champ, lets give this another try.')
			print('What will it be?')
			player_pos[0] -= nav['{}x'.format(user_input.lower())]
			player_pos[1] -= nav['{}y'.format(user_input.lower())]
	else:
		print('You cant do that!')
	
	if player_pos == goalxy and goals_reached[0] == 0:
		goals_reached[0] = 1
		print('The sun comes out and it is too much to bear.')
		print('You seek shelter under an awning and \nsee it belongs to a book shop.')
		player_pos = [0,0]
	if player_pos == [0,0] and goals_reached[0] == 1:
		goals_reached[1] = 1
		print('What the hell, you can read.\n You venture inside.')

# Starting Message
print('You emerge from the deli with a strut in your stride.\nBut the sidewalk is a hostile and crowded land.')
print('It will take care to navigate it\n')
ps = [' ',' ',' ',' ',' ',' ']


# Start
while not goals_reached == [1,1]:
	walk()
	ps = [' ',' ',' ',' ',' ',' ']


############################### END OF SCENE TWO #############################

print('Suddenly aliensa descend from the sky and kill\neveryone who has ever entered a book shop.')
print('Congratulations, you are dead.')

