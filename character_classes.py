'''
Moataz Khallaf
Character classes
2020/01/28

Contributors: Dhiraj Meenavilli -> Hit function
              Zeeshan Hooda     -> Refactor using pandas
'''

import pandas as pd
import random

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
                self.hp = self.stats['HP']

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


if __name__ == "__main__":
    import pandas as pd
    unit_stats = pd.read_csv('unitStats.csv')
    test_repr = []
    for i in range(0, 16):
        test_repr.append(Character(i, unit_stats))
    for i in range(len(test_repr)):
        print(test_repr[i])
    print(test_repr[0].get_unit_stats().head())