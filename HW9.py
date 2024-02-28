# File: HW9
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 11/13/2023

# Description of program: 
# Creates a character superclass that hero and enemy subclasses inherit from to create enemies and heros to play
# an rpg game with

# Scource Citing:
# Looked at lecture notes. Looked online at python library. Looked at play.rpg game

class Character:

    def __init__(self, name, health):
        """
        initializes variables

        :name: String. name of your character
        :health: int. the health number

        :return: No Return
        """  
        self.name = name
        self.health = health

    def __str__(self):        
        """
        Gives a formatted print statement to avoid bad formatting

        :return: formatted print statement showign the name and health of the character
        """  
        return(f'{self.name} (health={self.health})')

    def take_damage(self, damage):
        """
        Deals damage to the character the method is called on

        :damage: int. the damage amount
        :return: the updated health value after the damage has been dealt
        """ 
        self.health -= damage
        return(self.health)

class Hero(Character):

    def __init__(self, name, health):
        """
        initializes the Hero's variables by inheriting from the Character Class

        :name: initialized in Character class
        :health: initialized in Character class

        :return: No return
        """ 
        Character.__init__(self, name, health)
        self.__inventory = [] # initializes empty inventory list as a private variable to prevent bad cheating

    def restore_health(self, healing):
        """
        Heals the Hero for the specified health amount

        :healing: the amount to heal the Hero by

        :return: updated health amount after Hero health has healed
        """ 
        self.health +=  healing
        return(self.health)
    
    def add_inventory(self, item):
        """
        Adds an item to a Hero's inventory

        :item: the name of the item added to the inventory

        :return: No return
        """ 
        self.__inventory.append(item)

    def remove_inventory(self, item):
        """
        Checks to see if a Hero has an item in their inventory before removing it

        :item: the name of the item removed from the inventory

        :return: No return
        """ 
        if item in self.__inventory:
            self.__inventory.remove(item)

    def get_inventory(self):
        """
        'Gets' the inventory of a Hero

        :return: the inventory list
        """ 
        return(self.__inventory)
    
class Enemy(Character):

    def __init__(self, name, health, damage):
        """
        initializes the Enemy's variables

        :name: the name of the Enemy
        :health: the health of the Enemy 
        :damage: the damage the Enemy inflicts

        :return: No return
        """ 
        self.name = name
        self.health = health
        self.damage = damage

def main():
    """
    Creates a Hero and a couple enemies that do a couple battles. The hero gets an elixer to heal and a few items
    
    :return: No return
    """ 
    han = Hero("Han", 40)
    zombie = Enemy("Zombie", 20, 15)
    werewolf = Enemy("Werewolf", 15, 10)
    
    print("Start:")
    print(han)
    print(zombie)
    print(werewolf)

    werewolf.take_damage(10)
    han.take_damage(10)

    print("Battle 1:")
    print(han)
    print(werewolf)

    zombie.take_damage(20)
    han.take_damage(15)

    print("Battle 2:")
    print(han)
    print(zombie)

    han.add_inventory("5 Health Elixer")
    han.restore_health(5)
    han.remove_inventory("5 Health Elixer")

    print("Restore Health:")
    print(han)

    han.add_inventory("gold coin")
    han.add_inventory("candle")

    print("Inventory:")
    print(han.get_inventory())


if __name__ == "__main__":
    main()