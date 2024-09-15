import random
import time

from actors import Creature, Wizard, SmallAnimal, Dragon

def print_header():
    print()
    print('-----------------------------------------------------------------------')
    print()
    print('''
       (  )   /\   _                 (
        \ |  (  \ ( \.(               )                      _____
      \  \ \  `  `   ) \             (  ___                 / _   \\
     (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
    - .-               \+  ;          (  O                           \____
         WIZARD BATTLE        )        \_____________  `              \  /
    (__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
    (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
      .    /./.+-  . .- /  +--  - .     \______________//_              \_______
      (__ ' /x  / x _/ (                                  \___'          \     /
     , x / ( '  . / .  /                                      |           \   /
        /  /  _/ /    +                                      /              \/
       '  (__/                                             /                  \\
        ''')
    print()
    print('-----------------------------------------------------------------------')
    print()


def start_game():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 10),
        Dragon('Dragon', 50, 75, True),
        Wizard('Dark Wizard', 200)
    ]

    wizard = Wizard('Gandalf', 100)


    while True:
        active_creature = random.choice(creatures)
        print(f" Wizard {wizard.name} sees Creature {active_creature.name} of Level {active_creature.level}")

        cmd = input(" Do you Want to [a]ttack, or [r]un away, [l]ook around: ")
        if cmd == 'a':
            if wizard.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'l':
            print(f"The wizard {wizard.name} takes in the surroundings and sees:")
            for c in creatures:
                print(f" Creature {c.name} with Level {c.level}")

        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("All The Creatures are Defeated")
            break

        print()




    print("Wizard Run Away and you Lost the Game")



if __name__ == '__main__':
    print_header()
    start_game()
