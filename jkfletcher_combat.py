"""Turn-based combat game
Two characters fight until one 'dies'"""

import jkfletcher_tbc

def main():
    
    hero = jkfletcher_tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 20
    hero.hitChance = 60
    hero.maxDamage = 5
    hero.armor = 2
    
    monster = jkfletcher_tbc.Character()
    monster.name = "Monster"
    monster.hitPoints = 30
    monster.hitChance = 40
    monster.maxDamage = 8
    monster.armor = 0
    
    hero.printStats()
    monster.printStats()
    
    player1 = hero
    player2 = monster
    
    jkfletcher_tbc.fight(player1, player2)
    
if __name__ == "__main__":
    main()