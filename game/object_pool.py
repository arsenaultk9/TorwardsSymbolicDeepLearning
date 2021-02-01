layer_numbers = []
instances = dict([])

def register(instance, layer_number):
    if instances.get(layer_number) is None:
        instances[layer_number] = []
        layer_numbers.append(layer_number)

    instances[layer_number].append(instance)

def unregister(instance, layer_number):
    instances[layer_number].remove(instance)

def update():
    for layer_number in sorted(layer_numbers):
        for instance in instances[layer_number]:
            instance.update()

def draw(display_surface):
    for layer_number in sorted(layer_numbers):
        for instance in instances[layer_number]:
            instance.draw(display_surface)