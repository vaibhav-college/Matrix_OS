from crtarray import createarray

def opchecker(inp):

    var1 = ['A1', 'a1']

    var2 = ['L1', 'l1']

    var3 = ['D1', 'd1']

    if inp in var1:
        print('a1')
        return 'a1'
    
    elif inp in var2:
        print('l1')
        return 'l1'

    elif inp in var3:
        print('d1')
        return 'd1'


def listtraverser(index, storage, indexlst):

    k = storage[-1]

    storage.append(k[index])

    indexlst.append(index)

    if isinstance(storage[-1], list):

        for i in range(len(storage[-1])):

            print(i, ': ', storage[-1][i])


def compiler(db, indxlst, tmp, index, mode):
    if mode == 1:

        while len(tmp) > 1:

            for x in indxlst:

                if len(tmp) > 1:

                    g = tmp[-1]
                    tmp.pop(-1)
                    tmp[-1][x] = g

                    print(tmp)

                else: break

    elif mode == 2: 

        while len(tmp) > 1:
            tmp.pop(-1)
            tmp[-1][indxlst[0]] = None

            for x in indxlst:

                if len(tmp) > 1:

                    g = tmp[-1]
                    tmp.pop(-1)
                    tmp[-1][x] = g

                    print(tmp)
            
            break

def editdata(database):

    indexlst = []

    temp = []

    for i in range(len(database)):

        print(i, ': ', database[i])

    inpindex = int(input('Enter your index number: \n'))

    temp.append(database[inpindex])

    print(temp)

    if isinstance(temp[0], list) == False:
        op = input('What operation to perform? This code can do the following: \n\nFor Array\'s (A):\n1. Update array.\n\nFor list (L):\n1.Update list.\n\nFor deletion of data: \nType D1\n\nPlease put the operation syntax (A/L) before entering index data.')

        if opchecker(op) == 'a1':
            tmparray = []
            createarray(tmparray)
            print(temp)

            database[inpindex] = tmparray

        elif opchecker(op) == 'l1':

            tmplist = []

            amntofelem = int(input("How many amounts of elements in the list?"))

            for i in range(amntofelem):

                print("Enter your data for element ", i, " :")

                k = input()

                if k.isdigit():
                    k = int(k)

                tmplist.append(k)

            temp[-1] = tmplist

            database[inpindex] = tmplist

        elif opchecker(op) == 'd1':
            database[inpindex] = None

        print('Worked? : \n', temp)
    
    elif (isinstance(temp[0], list)) and (temp[0] == []):

        op = input('What operation to perform? This code can do the following: \n\nFor Array\'s (A):\n1. Update array.\n\nFor list (L):\n1.Update list.\n\nFor deletion of data: \nType D1\n\nPlease put the operation syntax (A/L) before entering index data.')

        indexlst.reverse()

        if opchecker(op) == 'a1':
            tmparray = []
            createarray(tmparray)
            temp[-1] = tmparray
            print(temp)

            compiler(database, indexlst, temp, inpindex, 1)

        elif opchecker(op) == 'l1':

            tmplist = []

            amntofelem = int(input("How many amounts of elements in the list?"))

            for i in range(amntofelem):

                print("Enter your data for element ", i, " :")

                k = input()

                if k.isdigit():
                    k = int(k)

                tmplist.append(k)

            temp[-1] = tmplist

            compiler(database, indexlst, temp, inpindex, 1)

        elif opchecker(op) == 'd1':
            compiler(database, indexlst, temp, inpindex, 2)

        print('Worked? : \n', temp)

    elif isinstance(temp[0][inpindex], list):

        contop = input('Continue indexing/traversing data or edit the current existing dataset? (Y/N)')

        while (contop == 'y') or (contop == 'Y'):

            if isinstance(temp[0][-1], list):

                for i in range(len(temp[-1])):

                    print(i, ': ', temp[-1][i])

            inpindex = int(input('Enter your index number: \n'))

            listtraverser(inpindex, temp, indexlst)
            print(temp, 'joe')

            contop = input('Continue indexing/traversing data or edit the current existing dataset? (Y/N)')

        op = input('What operation to perform? This code can do the following: \n\nFor Array\'s (A):\n1. Update array.\n\nFor list (L):\n1.Update list.\n\nFor deletion of data: \nType D1\n\nPlease put the operation syntax (A/L) before entering index data.')

        indexlst.reverse()

        if opchecker(op) == 'a1':
            tmparray = []
            createarray(tmparray)
            temp[-1] = tmparray
            print(temp)

            compiler(db=database, indxlst=indexlst, tmp=temp, index=inpindex, mode=1)

        elif opchecker(op) == 'l1':

            tmplist = []

            amntofelem = int(input("How many amounts of elements in the list?"))

            for i in range(amntofelem):

                print("Enter your data for element ", i, " :")

                k = input()

                if k.isdigit():
                    k = int(k) 

                tmplist.append(k)

            temp[-1] = tmplist

            compiler(database, indexlst, temp, inpindex, 1)

        elif opchecker(op) == 'd1':
            compiler(database, indexlst, temp, inpindex, 2)

        print('Worked? : \n', temp)