from data import locations, objects

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
    action = raw_input('Do you want to take the %s? Enter yes/no.\n' % object_name)
    if action == 'yes':
        if len(carrying) >= 4:
            print 'You are carrying too much. You need to put something down before you drop everything!'
        elif object_name == 'giraffe':
            print 'Don\'t be ridiculous. You can\'t pick up a giraffe, it\'s far too big!'
        else:
            carrying.append(object_name)
            if object_name == 'candyfloss':
                print 'That is disgusting. Why would you pick that up? But OK, you\'re in charge!'
            elif object_name == 'rat':
                print 'Seriously? Do you have any idea how many diseases it might be carrying? Be very careful!'
            print 'You take the %s.' % object_name
            print 'You are carrying:' + str(carrying)
            if object_name == 'cow' and 'loaf of bread' in carrying or object_name == 'loaf of bread' and 'cow' in carrying:
                print 'The cow is licking the bread. I wouldn\'t advise making a sandwich...'
            if object_name == 'penguin' and 'cow' in carrying or object_name == 'cow' and 'penguin' in carrying:
                print 'The cow and the penguin are whispering to each other. They are clearly up to something...'
    elif action == 'no':
        print 'You leave the %s where it is.' % object_name
        if len(carrying) == 0:
            print 'You are not carrying anything.'
        else:
            print 'You are carrying:' + str(carrying)
    else:
        print 'Sorry, I don\'t understand. Please enter yes/no.'
        pick_up_object()


def put_down_object():
    action = raw_input('Do you want to put anything down? Enter yes/no.\n')
    if action == 'yes':
        choice = raw_input('What do you want to put down? Enter an item that you are carrying.\n')
        if choice in carrying:
            object_name = choice
            carrying.remove(object_name)
            print 'You put down the %s.' % object_name
        else:
            print 'You are not carrying that. Let\s try that again!'
            put_down_object()
        if len(carrying) == 0:
            print 'You are not carrying anything.'
        else:
            print 'You are carrying:' + str(carrying)
    elif action == 'no':
        print 'OK, but don\'t blame me if your arms begin to ache!'
    else:
        print 'Sorry, I don\'t understand. Please enter yes/no.'
        put_down_object()


while True:
    place_name = locations[position]['place']
    place_desc = locations[position]['description']

    print 'You are at the %s.' % place_name
    if len(carrying) == 0:
        print 'You are not carrying anything.'
    else:
        print 'You are carrying:' + str(carrying)
    print '%s' % place_desc

    for k, v in objects.iteritems():
        if v['cur_location'] == position:
            object_name = objects[k]['name']
            object_desc = objects[k]['cur_desc']

            if object_name not in carrying:
                print '%s' % object_desc
                pick_up_object()

    if len(carrying) > 0:
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
        for k, v in objects.iteritems():
            if k in carrying:
                v['cur_location'] = position
                if v['cur_location'] != v['def_location']:
                    v['cur_desc'] = 'There is a ' + v['name'] + ' here which somebody has left behind. Was that you?!'
                else:
                    v['cur_desc'] = v['def_desc']
    else:
        print 'You cannot go that way! Choose a different direction.'