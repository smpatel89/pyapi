#!/usr/bin/python3

def showInstructions():
    print('''
RPG Game
=======
Grab the key and potion and go to the garden
Don\' die.

Commands:
    go [direction]
    get [item]
''')

def showStatus():
    print('------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('------------------------')

'''Test'''

inventory = []
rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'key'
            },
        'Kitchen': {
            'north': 'Hall',
            'item': 'monster'
            },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item': 'potion'
            },
        'Garden': {
            'north': 'Dining Room'
            }
        }

currentRoom = 'Hall'
showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('> ')
    
    move = move.lower().split()
    
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way')
    
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1])

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You have been eaten by a grue... GAME OVER!')
        break
