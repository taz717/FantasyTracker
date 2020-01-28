'''
Moataz Khallaf
Combat test using pandas
2020/01/27

Contributors: Zeeshan Hooda
'''

# imports
from random import randint 
import pandas as pd

# variables, lists and arrays

unit_stats = pd.read_csv('unitStats.csv')
# print(unit_stats.head())


# for i in range(len(unit_stats['TAG'])):
#     print(i, unit_stats['TAG'][i])
#     print(unit_stats.iloc[i])

# def get_unit(data, tag):
#     pass

class NPC:
    def __init__(self, tag, stat_list):
        """
        docstring
        """
        for i in range(len(stat_list['TAG'])):
            if stat_list['TAG'][i].lower() == tag.lower():
                self.stats = stat_list.iloc[i]

    def get_unit_stats(self):
        return self.stats


if __name__ == "__main__":
    ratogre = NPC('RatOgre', unit_stats)
    print(ratogre.get_unit_stats().values)


