# function defination
def checkList(sampleList):

    element = sampleList[0]
    flag = True

    # Comparing each element of list with first item
    for item in sampleList:
        if element != item:
            flag = False
            break

    if (flag == True):
        print("All elements are Equal")
    else:
        print("All elements are Not equal")


list1 = [1, 2, 3]
checkList(list1)   # Not Equal

list2 = [2, 2, 2]
checkList(list2)   # Equal
