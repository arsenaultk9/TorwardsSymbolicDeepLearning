instances = []
display_surface_instance = None

def register(instance):
    instances.append(instance)

def unregister(instance):
    instances.remove(instance)

def update():
    for instance in instances:
        instance.update()

def draw(display_surface):
    for instance in instances:
        instance.draw(display_surface)