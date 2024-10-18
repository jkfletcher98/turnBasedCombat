"""Module for turn-based combat system"""

import random
   
class Character(object):
    def __init__(self):
        super().__init__()
        self.name = "Test"
        self.hitPoints = 10
        self.hitChance = 50
        self.maxDamage = 5
        self.armor = 1
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            self.__hitPoints = value
        else:
            print("Hit Points must be an integer.")
            self.__hitPoints = 1
            
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value, min = 0, max = 100, default = 0):
        self.__hitChance = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    self.__hitChance = value
                else:
                    print("Hit Chance is too high")
            else:
                print("Hit Chance is too low")
        else:
            print("Hit Chance must be an integer")
            
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value > 0:
                self.__maxDamage = value
            else:
                print("Max Damage must be positive.")
                self.__maxDamage = 1
        else:
            print("Max Damage must be an integer.")
            self.__maxDamage = 1
            
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                self.__armor = value
            else:
                print("Armor must be positive.")
                self.__armor = 0
        else:
            print("Armor must be an integer.")
            self.__armor = 0
            
            
    def printStats(self):
        print(self.name)
        print("===============")
        print(f"Hit Points: {self.hitPoints}")
        print(f"Hit Chance: {self.hitChance}")
        print(f"Max Damage: {self.maxDamage}")
        print(f"Armor: {self.armor}")
        print()
        
    def hit(self, enemy):
        attack = random.randint(0,100)
        if attack < self.hitChance:
            print(f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print(f"for {damage} point(s) of damage!")
            if enemy.armor > 0:
                damage = damage - enemy.armor
                print(f"{enemy.name}'s armor absorbs {enemy.armor} points")
            if damage < 0:
                damage = 0
            enemy.hitPoints = enemy.hitPoints - damage
        else:
            print(f"{self.name} misses {enemy.name}")
            
            
def fight(player1, player2):
    keepGoing = True
    while keepGoing:
        print()
        player1.hit(player2)
        player2.hit(player1)
        
        print()
        
        if player1.hitPoints <= 0:
            print(f"{player1.name} is dead. {player2.name} wins!")
            keepGoing = False
        elif player2.hitPoints <= 0:
            print(f"{player2.name} is dead. {player1.name} wins!")
            keepGoing = False
        else:
            print(f"{player1.name}: {player1.hitPoints}")
            print(f"{player2.name}: {player2.hitPoints}")
            userClick = input("Press 'enter' for another round.")
        