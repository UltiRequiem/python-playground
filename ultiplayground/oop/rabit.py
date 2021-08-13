from .animal import GenericAnimal


class Rabbit(GenericAnimal):
    def __init__(self, name, speed=0) -> None:
        super().__init__(name, speed=speed)

    def hide(self):
        print(f"{self.name} hides!")


if __name__ == "__main__":
    my_rabbit = Rabbit("Alen")
    print(my_rabbit)
    my_rabbit.hide()
