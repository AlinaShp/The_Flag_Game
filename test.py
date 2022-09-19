import pandas as pd
import os
import random
import json


def convert_data_lists_to_srt(game_data):
    game_data = json.dumps(game_data)

    return game_data
def main2():
    data = [('Peter', 18, 7),
            ('Riff', 15, 6),
            ('John', 17, 8),
            ('Michel', 18, 7),
            ('Sheli', 17, 5)]
    data2=[('hhhhh', 18, 7),
            ('hhh', 15, 6),
            ('hhh', 17, 8),
            ('Michel', 18, 7),
            ('Sheli', 17, 5)]
    emptylist = []
    string=""

    list1=convert_data_lists_to_srt(data)
    list2=convert_data_lists_to_srt(data2)

    for row in range (len(data)):
        for col in range(len(data[row])):
            string=string+str(data[row][col])+","
            emptylist.append(string)

  #  print(emptylist)
    list=[list1], [list2]

   # print(list)
    string=""

   # print(emptylist)


    df = pd.DataFrame(list)
    print(df)

if __name__ == '__main__':
    main2()