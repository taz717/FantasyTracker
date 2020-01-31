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

                # stuff that gets pulled out of the csv
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

                 # just random stuff

    def get_unit_stats(self):
        """
        The method to get the Character stats.

        Returns:
            stats (pd.df): The stats of the character.
        """
        return self.stats

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

        choice = input("What would you like to do?")
        for i in range(len(self.stats)):
            if choice == self.stats[i] and choice == self.basic:
                dmg = random.randrange(1, int(self.dmg))

                if dmg != int(dmg):
                    dmg = int(round(dmg) + 1)

                return dmg

            elif choice == self.stats[i] and choice == self.blight:  # if the choice and ability match
                dmg = [(random.randrange(1, int(self.dmg)) * (1 - (self.blight_dmg_mod / 100)))
                        , (self.blight_chance /100)
                        , self.blight_dot]  # send back dmg, %chance to apply effect and DOT

                if dmg[0] != int(dmg[0]):
                    dmg[0] = int(round(dmg[0]) + 1)

                return dmg

            elif choice == self.stats[i] and choice == self.bleed:
                dmg = [(random.randrange(1, int(self.dmg)) * (1 - (self.bleed_dmg_mod / 100)))
                        , (self.bleed_chance / 100)
                        , self.bleed_dot]

                if dmg[0] != int(dmg[0]):
                    dmg[0] = int(round(dmg[0]) + 1)

                return dmg

            elif choice == self.stats[i] and choice == self.stats[24]:
                dmg = [(random.randint(1, int(self.dmg) * (1 - self.move_dmg_mod / 100)))
                       , (self.move_chance / 100)]

                if dmg[0] != int(dmg[0]):
                    dmg[0] = int(round(dmg[0]) + 1)

                return dmg


# _____________ Functions _______________

def partition(li, first, last):
    '''
    This was written back in zhang's comp sci class, I just borrowed the code I wrote before
    :param li:
    :param first:
    :param last:
    :return:
    '''
    pivotVal = li[first]

    leftMark = first + 1
    rightMark = last

    done = False
    while not done:

        while leftMark <= rightMark and li[leftMark] <= pivotVal:
            leftMark += 1

        while rightMark >= leftMark and li[rightMark] >= pivotVal:
            rightMark -= 1

        if rightMark < leftMark:  # stopping case in iteration itself
            done = True

        else:
            temp = li[leftMark]
            li[leftMark] = li[rightMark]
            li[rightMark] = temp

    temp = li[first]
    li[first] = li[rightMark]  #li[first], li[rightMark] = li[rightMark], li[first]
    li[rightMark] = temp

    return rightMark

def quickSort(li, first, last):
    '''
    This was written back in zhang's comp sci class, I just borrowed the code I wrote before
    :param li:
    :param first:
    :param last:
    :return:
    '''
    if first < last:  # stopping case
        splitPoint = partition(li, first, last)

        quickSort(li, first, splitPoint -1)
        quickSort(li, splitPoint +1, last)



def initiative(party1, party2):
    '''
    This rolls a random number between 1 and the max speed someone can have per turn then creates a
    different array that has the order of the fight happening rn
    :param party1:
    :param party2:
    :return:
    '''
    party1_speed = []
    party2_speed = []
    for i in range(len(party1)):
        temp_spd = random.randint(1, party1[i].spd)
        party1_speed.append([temp_spd, party1[i].tag])

    for i in range(len(party2)):
        temp_spd = random.randint(1, party1[i].spd)
        party2_speed.append([temp_spd, party1[i].tag])

    total_party = party1_speed+party2_speed
    (quickSort(total_party, 0, len(total_party) - 1))
    return total_party

def hit(acc, dodge):
    acc = random.randint(acc, 100)
    dodge = random.randint(dodge, 100)
    if acc - dodge >= 1:
        itHit = 1
    else:
        itHit = 0

    return itHit

# _____________ TEST _______________

if __name__ == "__main__":

    import pandas as pd
    unit_stats = pd.read_csv('unitStats.csv')
    test_repr1 = []
    test_repr2 = []

    for i in range(0, 4):
        test_repr1.append(NPC(i, unit_stats))
    for i in range(0, 4):
        test_repr2.append(NPC(i, unit_stats))

    total_party = initiative(test_repr1, test_repr2)




    #
    # test = NPC(0, unit_stats)
    # test1 = NPC(0, unit_stats)
    # if hit(test.acc, test1.dodge):
    #     print(test.get_unit_stats())
    #     print(test.use_ability())