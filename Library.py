'''
Moataz Khallaf
Library
2020/01/28

Contributors: Dhiraj Meenavilli -> Hit function
              Zeeshan Hooda     -> Refactor using pandas
'''

import pandas as pd
import random

# _____________ Classes _______________

class Character:
    """ 
    This is a class for general characters. 

    Attributes: 
        stats (pd.df): The stats of the character. 
        id (int): The ID of the character.
        hp (int): The HP of the character.
    """
    def __init__(self, id, stat_lsit):
        """
        The constructor method for Character class.

        Parameters:
            id (int): The ID of the character.
            stats (pd.df): The stats of the character.
        """
        for unit in range(len(stat_lsit['ID'])):
            if stat_lsit['ID'][unit] == id:
                self.id = id
                self.stats = stat_lsit.iloc[unit]
                self.race = self.stats['RACE']
                self.tag = self.stats['TAG']
                self.hp = self.stats['HP']
                self.max_hp = self.stats['MAXHP']
                self.dmg = self.stats['DMG']
                self.acc = self.stats['ACC']
                self.spd = self.stats['SPD']
                self.dodge = self.stats['DODGE']
                self.prot = self.stats['PROT']
                self.bleed_res = self.stats['BleedRES']
                self.blight_res = self.stats['BlightRES']
                self.move_res = self.stats['MoveRES']
                self.stun_res = self.stats['StunRES']
                self.actions = self.stats['Actions']

    def get_unit_stats(self):
        """
        The method to get the Character stats.

        Returns:
            stats (pd.df): The stats of the character.
        """
        return self.stats

    def use_ability(self):
        """
        The function to use a characters
        """
        """
        overview: Lets the unit use an ability from the stat list it's assigned
        input: ability choice
        output: ability stats
        :return:
        """
        print(self.stats)
        choice = input("What would you like to do?")
        for i in range(len(self.stats)):
            if choice == self.stats[i] and choice == self.stats[15]:
                dmg = random.randrange(1, int(self.stats[9]))
                print(dmg)

            elif choice == self.stats[i] and choice == self.stats[16]:  # if the choice and ability match
                dmg = [(random.randrange(1, int(self.stats[9])) * (1 - (self.stats[18] / 100)))
                        , (self.stats[17])
                        , self.stats[19]]  # send back dmg, %chance to apply effect and DOT

            elif choice == self.stats[i] and choice == self.stats[20]:
                dmg = [(random.randrange(1, int(self.stats[9])) * (1 - (self.stats[22] / 100)))
                        , (self.stats[21] / 100)
                        , self.stats[24]
                        ]
            elif choice == self.stats[i] and choice == self.stats[24]:
                # added random end range value because it was missing
                # change later to correct range
                dmg = [(random.randint(1, 2))]

    def __repr__(self):
        return str(self.stats.values.tolist())

    def __str__(self):
        return str(self.stats.values.tolist())

class NPC(Character):
    def __init__(self, id, stat_lsit):
        Character.__init__(self, id, stat_lsit)
        self.type = self.stats['Type']
        self.basic = self.stats['Basic']
        self.blight = self.stats['Blight']
        self.blight_chance = self.stats['Blight%Chance']
        self.blight_dmg_mod = self.stats['blightDMGMod%']
        self.blight_dot = self.stats['blightDOT']
        self.bleed = self.stats['Bleed']
        self.bleed_chance = self.stats['Bleed%Chance']
        self.bleed_dmg_mod = self.stats['bleedDMGMod%']
        self.bleed_dot = self.stats['bleedDOT']
        self.stun = self.stats['Stun']
        self.stun_chance = self.stats['Stun%Chance']
        self.stun_dmg_mod = self.stats['stunDMGMod']
        self.move = self.stats['Move']
        self.move_chance = self.stats['Move%Chance']
        self.move_dmg_mod = self.stats['moveDMGMod']



# _____________ Functions _______________

def hit(acc, dodge):
    acc = random.randrange(acc, 100)
    dodge = random.randrange(dodge, 100)
    if acc - dodge >= 1:
        itHit = 1
    else:
        itHit = 0

    return itHit

# _____________ TEST _______________

if __name__ == "__main__":
    import pandas as pd
    unit_stats = pd.read_csv('unitStats.csv')
    test_repr = []
    for i in range(0, 16):
        test_repr.append(NPC(i, unit_stats))
    for i in range(len(test_repr)):
        print(test_repr[i])
    print(test_repr[0].get_unit_stats().head())