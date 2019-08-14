'''
   adventure.py
   A small text adventure game I made back in the day.

   Copyright 2013, Michael Pascale
'''

score = 0
secretpassage = 0
lamp = 0

def welcomemessage():
	print 'Adventure! - By Michael Pascale, September 12th 2013'
	print 'Commands:'
	print ' go.......(north, south, east, west, up, down)'
	print ' take.....(object)'
	print ' use......(object)'
	print ''
	nspassage()

def die():
	print 'You will now time travel back to the beginning of your adventure.'
	print '...'
	global score
	score = score - 5
	nspassage()

def nspassage():
	print 'You are in a tunnel that runs from North to South.'
	command = raw_input('> ')
	if command == 'go north':
		if lamp == 1:		
			abandonedminenolamp()
		else:
			abandonedmine()
	elif command == 'go south':
		abyssstairs()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		nspassage()

def abandonedmine():
	print 'You are in what appears to be an abandoned mine.' 
	print 'There is a low passage in the east.'
	print 'There is a lamp here.'
	print 'A tunnel exits from the South.'
	command = raw_input('> ')
	if command == 'go south':
		nspassage()
	elif command == 'go east':
		supplyroom()
	elif command == 'take lamp':
		global lamp
		global score
		lamp = 1
		score = score + 5
		abandonedminenolamp()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		abandonedmine()

def abandonedminenolamp():
	print 'You are in what appears to be an abandoned mine.' 
	print 'There is a low passage in the east.'
	print 'A tunnel exits from the South.'
	command = raw_input('> ')
	if command == 'go south':
		nspassage()
	elif command == 'go east':
		supplyroom()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		abandonedminenolamp()

def supplyroom():
	print 'You are in a small supply room adjacent to the mine.'
	print 'A note on the wall says "Say: rr"'
	command = raw_input('> ')
	if command == 'go west':
		if lamp == 1:		
			abandonedminenolamp()
		else:
			abandonedmine()
	elif command == 'rr':
		if secretpassage == 1:
			print 'You have teleported!'		
			readingroomnobook()
		else:
			readingroom()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		supplyroom()

def abyssstairs():
	print 'You are at the top of a stairway going down into an abyss.'
	print 'There is a tunnel in the North.'
	command = raw_input('> ')
	if command == 'go north':
		nspassage()
	elif command == 'go down':
		cavernpassage()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		abyssstairs()

def cavernpassage():
	print 'You are on a stairway going into the abyss.'
	print 'The stairs continue out of sight.'
	print 'There is a passage on your West side.'
	command = raw_input('> ')
	if command == 'go down':
		print 'You fell off the stairs and died!'
		die()
	elif command == 'go west':
		cavern()
	elif command == 'go up':
		abyssstairs()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernpassage()

def cavern():
	print 'You are in a large cavern.'
	print 'There is a passage on the East side.'
	print 'The cavern extends in all directions (except East).'
	command = raw_input('> ')
	if command == 'go north':
		if lamp == 1:
			cavernnorthlight()
		else:
			cavernnorthdark()
	elif command == 'go west':
		cavernwest()
	elif command == 'go south':
		cavernsouth()
	elif command == 'go east':
		cavernpassage()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavern()

def cavernnorthdark():
	print 'It is too dark to go any further'
	print 'If only you had a light source of some kind...'
	command = raw_input('> ')
	if command == 'go south':
		cavern()
	elif command == 'go south':
		cavern()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernnorthdark()

def cavernnorthlight():
	print 'You are in the Northern part of the cavern.'
	print 'There are gold coins here.'
	print 'You have reached a dead end.'
	command = raw_input('> ')
	if command == 'go south':
		cavern()
	elif command == 'take coins':
		score = score + 5
		cavernnorthnocoins()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernnorthlight()

def cavernnorthnocoins():
	print 'You are in the Northern part of the cavern.'
	print 'It is a dead end.'
	command = raw_input('> ')
	if command == 'go south':
		cavern()
	elif command == 'go south':
		cavern()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernnorthnocoins()

def cavernsouth():
	print 'You are in the Southern side of the cavern.'
	print 'It is a dead end.'
	command = raw_input('> ')
	if command == 'go north':
		cavern()
	elif command == 'go north':
		cavern()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernsouth()

def cavernwest():
	print 'This is the West side of the cavern.'
	print 'There is a passage here that leads even further west.'
	print 'The cavern extends into the East.'
	command = raw_input('> ')
	if command == 'go west':
		if secretpassage == 1:		
			readingroomnobook()
		else:
			readingroom()
	elif command == 'go east':
		cavern()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		cavernwest()

def readingroom():
	print 'You are in a reading room with a small collection of books.'
	print 'There is a book on the ground.'
	print 'Passages exit to the North and South.'
	print 'A note on the wall says "Say sr"'
	command = raw_input('> ')
	if command == 'go north':
		cavernwest()
	elif command == 'sr':
		print 'You have teleported'
		supplyroom()
	elif command == 'go south':
		lake()
	elif command == 'take book':
		print 'The book is attached to a lever under the floor.'
                print 'When you attempt to take the book a lever is pulled.'
		print 'A loud rumbling noise can be heard from the South.'
		print ''
		global secretpassage
		global score
		score = score + 5
		secretpassage = 1
		readingroomnobook()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		readingroom()

def readingroomnobook():
	print 'You are in a reading room with a small collection of books.'
	print 'Passages exit to the North and South.'
	print 'A note on the wall says "sr"'
	command = raw_input('> ')
	if command == 'go north':
		cavernwest()
	elif command == 'sr':
		supplyroom()
	elif command == 'go south':
		lake()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		readingroomnobook()

def lake():
	print 'You are standing at the edge of an underground lake.'
	print 'A trail goes East towards a small beach.'
	print 'A passage leads North.'
	print 'There is a boat here.'
	command = raw_input('> ')
	if command == 'go north':
		if secretpassage == 1:		
			readingroomnobook()
		else:
			readingroom()
	elif command == 'go east':
		beach()
	elif command == 'use boat':
		village()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		lake()

def beach():
	print 'You are at the beach.'
	print 'This appears to be a dead end.'
	command = raw_input('> ')
	if command == 'go west':
		lake()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		beach()

def village():
	print 'You are standing in the middle of a dwarf village near the lake.'
	print 'The dwarves disappear as soon as they see you.'
	print 'A boat is sitting on the shore.'
	print 'A system of tiny roads go off in all directions'
	command = raw_input('> ')
	if command == 'go north':
		waterfall()
	elif command == 'go south':
		dwarves1()
	elif command == 'go east':
		dwarves2()
	elif command == 'go west':
		dwarves()
	elif command == 'use boat':
		lake()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		village()

def dwarves1():
	print 'You have found a dwarves hiding place!'
	print 'The dwarf shot you and you died!'
	die()

def dwarves2():
	print 'You are standing near a river leading to the lake.'
	print 'You have found a dwarves hiding place!'
	print 'The dwarf shot you and you died!'
	die()

def waterfall():
	global secretpassage 
	if secretpassage == 0: 
		waterfallclosed()
	elif secretpassage == 1:
		waterfallopen()

def waterfallclosed():
	print 'You are standing near a large waterfall.'
	print 'The waterfall leads to a stream that provides water to the village and the lake.'
	print 'A tiny road goes to the dwarf village in the South.'
	print 'This appears to be a dead end.'
	command = raw_input('> ')
	if command == 'go south':
		village()
	elif command == 'go south':
		village()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		waterfallclosed()

def waterfallopen():
	print 'You are standing near a large waterfall.'
	print 'A rock is parting the water revealing a passage behind the waterfall on your East side.' 
	print 'The waterfall leads to a stream that provides water to the village and the lake.'
	print 'A tiny road goes to the dwarf village in the South.'
	command = raw_input('> ')
	if command == 'go south':
		village()
	elif command == 'go east':
		treasureroom()
	else:
		print 'That command does not exist for this location.'
		print 'I will repeat the description of your location.'
		print '...'
		waterfallopen()

def treasureroom():
	print 'Congratulations, you have found the treasure room!'
	global score
	score = score + 5
	print 'Your score:'
	print score
	print ''
	print 'Thank you for playing!'
	print ''
	print ''
	welcomemessage()
welcomemessage()



