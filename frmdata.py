import pandas as pd
import numpy as np

def framedata(database):

    temp = np.array(database)

    # for i in range(len(database)):
    #     a = database[i]
    #     g = list(a)
    #     temp.append(g)

    database = pd.DataFrame(temp).swapaxes("index", "columns")

    database.index.name = 'Array number'

    print('Dataframe: \n\n', database)

    savefile = input('Save the file as a CSV? (Y/N): ')

    if (savefile == 'Y') or (savefile == 'y'):
        directory = input("Enter the directory please: ")

        database.to_csv(directory)
        print('saved')
    else:
        pass