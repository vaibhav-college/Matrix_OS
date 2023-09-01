import numpy as np

def createarray(database):

    temp = []

    rowcount = 0
    colcount = 0

    timesrow = int(input('How many rows in DataSet1: '))
    timescolumn = int(input('How many columns in DataSet1: '))

    for i in range(timesrow*timescolumn):
        if (colcount >= timescolumn) == True:
            colcount = 0
            rowcount += 1
    
        print('Element at Column ', colcount, ' at row ', rowcount, ' : ')
    
        colcount += 1

        inp = int(input(''))

        temp.append(inp)
    
    temparray = np.array(temp, dtype=object).reshape(timesrow, timescolumn)

    database.append(temparray.copy())

    return temparray