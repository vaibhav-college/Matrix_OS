def createindex(database, mode):

    op = int(input("How many new lists to create?\n"))
    temp = []
    temp2 = []

    if mode == 1:

        for i in range(op):
            database.append(temp)

    elif mode == 2:

        for i in range(op):
            temp.append(temp2)
        
        database.append(temp2)

    print('Appended ', op, ' amount of lists')

    return temp