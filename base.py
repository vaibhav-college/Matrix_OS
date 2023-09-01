import time

from crtarray import createarray
from crtind import createindex
from edtdat import editdata
from frmdata import framedata

arraydatabase = [1,2,[3,4,[5,6]]]

def baserunner():
    para = input('Would you like to continue editing? (Y/N)')

    if (para == 'y') or (para == 'Y'):
        return 'yes'
    else:
        print('Exiting in 3 seconds')
        time.sleep(3)
        exit()

while baserunner() == 'yes':
    opinp = int(input('Welcome!\nWhat would you like to do? This code can do the following: \n\n1. Create array.\n2. Create indexes/lists.\n3. Edit pre-existing data.\n4. Frame the data into panda\'s dataframe.\n5. Print data.\n\n'))

    if opinp == 1 :
        createarray(arraydatabase)
    
    elif opinp == 2 :
        createindex(arraydatabase, 1)
    
    elif opinp == 3:
        editdata(arraydatabase)

    elif opinp == 4:
        framedata(arraydatabase)

    elif opinp == 5:
        print(arraydatabase)