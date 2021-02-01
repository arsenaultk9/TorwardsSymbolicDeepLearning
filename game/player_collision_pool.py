possible_collision_events = []

def register(player, other_object, action):
    def colision_event():
        if player.is_colliding_with(other_object):
            action()

    possible_collision_events.append(colision_event)


def update():
    for possible_event in possible_collision_events:
        possible_event()