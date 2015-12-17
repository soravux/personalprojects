room_list = []
room = ['This is the second bedroom', 3, 1, None, None]
room_list.append(room)
room = ['This is the south hall', 4, 2, None, 0]
room_list.append(room)
room = ['This is the dining room', 5, None, None, 1]
room_list.append(room)
room = ['This is the first bedroom', None, 4, 0, None]
room_list.append(room)
room = ['This is the north hall', 6, 5, 1, 3]
room_list.append(room)
room = ['This is the kitchen', None, None, 2, 4]
room_list.append(room)
room = ['This is the balcony', None, None, 4, None]
room_list.append(room)

current_room = 0
done = False

while not done:
    print(room_list[current_room][0])
    direction = input('What direction? ')
    next_room = None
    if direction.lower() == 'north' or direction.lower() == 'n':
        next_room = room_list[current_room][1]
    elif direction.lower() == 'east' or direction.lower() == 'e':
        next_room = room_list[current_room][2]
    elif direction.lower() == 'south' or direction.lower() == 's':
        next_room = room_list[current_room][3]
    elif direction.lower() == 'west' or direction.lower() == 'w':
        next_room = room_list[current_room][4]
    else:
        print("I don't understand :( ")

    if next_room == None:
        print("You can't go that way.")
    else:
        current_room = next_room
