class Animal:
    def sleep(self):
        print("Animal can sleep lie on the floor ")

    def eat(self):
        print("Animal can eat Burger")

    def height(self):
        print("animal has huge height ")

class Dog(Animal):
    def sleep(self):
        print("Dog can sleep by siting or laydown on floor")

class Horse(Animal):
    def sleep(self):
        print("Horse  can sleep by standing on floor")

class Snake(Animal):
    pass

animal = Animal()
animal.sleep()
animal.eat()
animal.height()

dog = Dog()
dog.sleep()
dog.eat()
dog.height()

horse = Horse()
horse.sleep()
horse.eat()
horse.height()

snake = Snake()
snake.sleep()
snake.eat()
snake.height()
