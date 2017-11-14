from data import locations

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)
carrying = []

while True:
    location = locations[position]['name']
    description = locations[position]['description']
    object = locations[position]['object']
    print 'You are at the %s.' % location
    print '%s' % description

    action = raw_input('Do you want to take the %s? Enter yes/no.' % object)

    if action == 'yes':
        carrying.append(object)
        print 'You take the %s.' % object
        print 'You have with you:' + str(carrying)
    elif action == 'no':
        print 'You leave the %s behind.' % object
        if len(carrying) == 0:
            print 'You have with you: nothing'
        else:
            print 'You have with you:' + str(carrying)
    else:
        print 'Sorry, I don\'t understand. Please enter yes/no.'

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'To the %s is a %s.' % (k, possible_location['name'])
            valid_directions[k] = possible_position

    direction = raw_input('Which direction do you want to go?\n')
    if direction in valid_directions:
        position = valid_directions[direction]
    else:
        print 'You cannot go that way! Choose a different direction.'
