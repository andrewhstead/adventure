from data import locations

directions = {
    'west': (-1, 0, 0),
    'east': (1, 0, 0),
    'north': (0, -1, 0),
    'south': (0, 1, 0),
    'up': (0, 0, 1),
    'down': (0, 0, -1),
}

position = (0, 0, 0)
carrying = []


def pick_up_object():
    action = raw_input('Do you want to take the %s? Enter yes/no.\n' % object)
    if action == 'yes':
        if len(carrying) >= 4:
            print 'You are carrying too much. You need to put something back where you found it!'
        else:
            carrying.append(object)
            if object == 'candyfloss':
                print 'That is disgusting. Why would you pick that up? But OK, you\'re in charge!'
            elif object == 'rat':
                print 'Seriously? Do you have any idea how many diseases it might be carrying? Be very careful!'
            print 'You take the %s.' % object
            print 'You are carrying:' + str(carrying)
            if object == 'cow' and 'bread' in carrying or object == 'bread' and 'cow' in carrying:
                print 'The cow is licking the bread. I wouldn\'t advise making a sandwich...'
            if object == 'penguin' and 'cow' in carrying or object == 'cow' and 'penguin' in carrying:
                print 'The cow and the penguin are whispering to each other. They are clearly up to something...'
    elif action == 'no':
        print 'You leave the %s behind.' % object
        if len(carrying) == 0:
            print 'You are not carrying anything.'
        else:
            print 'You are carrying:' + str(carrying)
    else:
        print 'Sorry, I don\'t understand. Please enter yes/no.'
        pick_up_object()


def put_down_object():
    action = raw_input('Do you want to put down the %s? Enter yes/no.\n' % object)
    if action == 'yes':
        carrying.remove(object)
        print 'You put down the %s.' % object
        if len(carrying) == 0:
            print 'You are not carrying anything.'
        else:
            print 'You are carrying:' + str(carrying)
    elif action == 'no':
        print 'You have with you:' + str(carrying)
    else:
        print 'Sorry, I don\'t understand. Please enter yes/no.'
        put_down_object()

while True:
    place = locations[position]['place']
    place_desc = locations[position]['place_desc']
    object = locations[position]['object']
    object_desc = locations[position]['object_desc']
    print 'You are at the %s.' % place
    print '%s' % place_desc
    if object not in carrying:
        print '%s' % object_desc
        pick_up_object()

    else:
        print 'You have with you:' + str(carrying)
        put_down_object()

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1], position[2] + v[2])
        possible_location = locations.get(possible_position)
        if possible_location:
            print '%s from here is the %s.' % (k, possible_location['place'])
            valid_directions[k] = possible_position

    direction = raw_input('Which direction do you want to go?\n')
    if direction in valid_directions:
        position = valid_directions[direction]
    else:
        print 'You cannot go that way! Choose a different direction.'
