#Doggy age


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor


dog = Dog(dog_age=33)
print(dog.human_age())
