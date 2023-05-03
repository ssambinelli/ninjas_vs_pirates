from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

print('Welcome to FantasyLand, you are a Ninja')

while michelangelo.health > 0 and jack_sparrow.health > 0:
    choice = input('Choose an action \n 1)Attack \n 2)Use special\n 3)Power Up\n')
    if choice == '1':
        michelangelo.attack(jack_sparrow)
    elif choice == '2':
        michelangelo.use_special()
    elif choice == '3':
        michelangelo.power_up()
    else:
        print('Invalid choice\n')
        continue
    
    jack_move = random.randint(1,3)
    if jack_move == 1:
        jack_sparrow.attack(michelangelo)
    elif jack_move == 2:
        jack_sparrow.use_special()
    elif jack_move == 3:
        jack_sparrow.power_up()

        
    if michelangelo.health ==0:
        print('You lose!')
    elif jack_sparrow.health ==0:
        print('You win!')

    

        