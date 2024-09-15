import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # def __repr__(self):
    #     return f"Creature: {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1,12) * self.level



class Wizard(Creature):

    def attack(self, creature):
        print(f"Wizard {self.name} Attacks the Creature {creature.name}")

        wizard_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print(f" Wizard {self.name} rolled {wizard_roll}")
        print(f" Creature {creature.name} rolled {creature_roll}")
        if wizard_roll >= creature_roll:
            print(f"The wizard has handily triumphed over {creature.name}")
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2



class Dragon(Creature):
    def __init__(self, name, the_level, scaliness, breath_fire):
        super().__init__(name, the_level)
        self.scale_thickness = scaliness
        self.breath_fire = breath_fire


    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()

        fire_modifier = 5  if self.breath_fire else 1
        scale_modifier = self.scale_thickness / 10

        return base_roll * fire_modifier * scale_modifier
