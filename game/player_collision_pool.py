class PlayerCollisionPool:
    possible_collision_events = dict([])
    events_to_cancel = []

    @classmethod
    def register(cls, player, other_object, action):
        def colision_event():
            if player.is_colliding_with(other_object):
                action()

        cls.possible_collision_events[other_object] = colision_event

    @classmethod
    def unregister(cls, other_object):
        cls.events_to_cancel.append(other_object)

    @classmethod
    def update(cls):
        for possible_event in cls.possible_collision_events.values():
            possible_event()

        for event_to_cancel in cls.events_to_cancel:
            del cls.possible_collision_events[event_to_cancel]

        cls.events_to_cancel = []
