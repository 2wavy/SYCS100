#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler
waveList = [3,4,6,8,9]


def binarySearch(MyPurpose, waveList):
    Discovery = False
    bottom = 0
    top = len(waveList) - 1
    if bottom == top:
        return -1
    while bottom<=top and not Discovery:
        mid = (bottom+top)//2
        if waveList[mid]==MyPurpose:
            Discovery = True
        elif waveList[mid] < MyPurpose:
            bottom = mid + 1
        else:
            top = mid - 1
    return Discovery

    print binarySearch(MyPurpose, waveList)
