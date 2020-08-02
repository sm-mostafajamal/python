class Dog:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes/ Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
phill = Dog("phill ", 5)
milky = Dog("heath ", 6)

# Access the instence Attribute
print("{}is {} and {} is {}".format(phill.name, phill.age, milky.name, milky.age))


# is philo a mammal
if phill.species == "mammal":
    print("{0}is a {1}".format(phill.name, phill.species, milky.name))  # indexing by the formate attribute

# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)


# Output
print("The oldest dog is {} years old.".format(
    get_biggest_number(phill.age, milky.age)))