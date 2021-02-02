class ObjectPool:
    layer_numbers = []
    instances = dict([])

    @classmethod
    def register(cls, instance, layer_number):
        if cls.instances.get(layer_number) is None:
            cls.instances[layer_number] = []
            cls.layer_numbers.append(layer_number)

        cls.instances[layer_number].append(instance)

    @classmethod
    def unregister(cls, instance, layer_number):
        cls.instances[layer_number].remove(instance)

    @classmethod
    def update(cls):
        for layer_number in sorted(cls.layer_numbers):
            for instance in cls.instances[layer_number]:
                instance.update()

    @classmethod
    def draw(cls, display_surface):
        for layer_number in sorted(cls.layer_numbers):
            for instance in cls.instances[layer_number]:
                instance.draw(display_surface)