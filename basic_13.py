# basic 13

# print 1-255
def print1to255():
    for x in range(1,256):
        print(x)

# print odds 1-255
def printOdds():
    for x in range(1,256):
        if x % 2 == 1:
            print(x)

# Print Ints and Sum 0-255
def pias255():
    sum = 0
    for x in range(0,256):
        print(x)
        sum = sum + x
        print(sum)

# iterate and print array
def PrintArrayVals(arr):
    for x in arr:
        print(arr[x-1])

# Find Print & Max
# def PrintMaxOfArray(arr):
#     max = arr[0]
#     for x in range(len(arr)):
#         if arr[x] > max:
#             max = arr[x]
#     print(max)

# Get and print average
def GetAndPrintAvg(arr):
    sum = 0
    for x in range(len(arr)):
        sum = sum + arr[x]
    print(sum/len(arr))

# Array with Odds
def roa1to255():
    arr = []
    for x in range(1,256):
        if x % 2 == 1:
            arr.append(x)
    print(arr)

# Square the values
def squareVals(arr):
    for x in range(len(arr)):
        arr[x] = arr[x] * arr[x]
    print(arr)

# Greater than Y
def greaterThanY(arr, y):
    count = 0
    for x in range(len(arr)):
        if arr[x] > y:
            count = count + 1
    print(count)

# zero out negative numbers
def zeroOut(arr):
    for x in range(len(arr)):
        if arr[x] < 0:
            arr[x] = 0
    print(arr)

# max min average
def maxMinAvg(arr):
    sum = 0
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
        sum = sum + i
    return {
        'max':max,
        'min':min,
        'avg':sum/len(arr)
    }

# shift array values
def shift(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    return arr

# swap string for array negative values
def swampString(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    return arr

