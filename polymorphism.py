"""
This is the parent/base/super class
"""
class Planet:
    def __init__(self, mass, spin, magnetic_field):
        self.mass = mass
        self.spin = spin
        self.magnetic_field = magnetic_field



# this is a subclass of planets, which includes the parent class attributes as well as attributes specific to the child class

class Goldilocks(Planet):
    def __init__(self, mass, spin, magnetic_field, life):
        # By using super, we don't need to explicitly initialize the parent class attributes
        super().__init__(mass, spin, magnetic_field)
        self.life = True


# Creation of our objects, first object refers to the parent class and the second object
# refers to the child class
mars = Planet(200, 50000, 15)

earth = Goldilocks(300, 25000, 500, True)


print(mars.mass)
print(earth.mass)


print(earth.life)
