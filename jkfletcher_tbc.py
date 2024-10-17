"""Module for turn-based combat system"""

import random

def main():
    hero = Character()
    hero.name = "Hero"
    hero.hitPoints = 20
    hero.hitChance = 60
    hero.maxDamage = 5
    hero.armor = 2
    
    monster = Character()
    monster.name = "Monster"
    monster.hitPoints = 30
    monster.hitChance = 40
    monster.maxDamage = 8
    monster.armor = 0
    
    hero.printStats()
    monster.printStats()
    
    
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
        
    def hit():
        strike = random.randint(0,100)
        #if strike is less than or equal to lower hitChance
        if strike <=
        #elif strike is less than or equal to higher hitChance
        elif strike <= 
        else:
            print("Both miss!")
        
            
main()