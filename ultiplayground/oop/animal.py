class GenericAnimal:
    def __init__(self, name, speed=0) -> None:
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name} is happy :)"

    def run(self, speed):
        self.speed = speed
        print(f"{self.name} runs with speed {self.speed}.")

    def stop(self):
        self.speed = 0
        print(f"{self.name} stands still.")


if __name__ == "__main__":
    my_generic_animal = GenericAnimal("A generic animal")
    print(my_generic_animal)
    my_generic_animal.run(3)
    my_generic_animal.stop()
