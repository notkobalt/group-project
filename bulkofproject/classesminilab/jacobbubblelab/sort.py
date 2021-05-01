import sys, time

input_array = []

i = 1
while i < len(sys.argv):
    input_array.append(int(sys.argv[i]))
    i += 1


def bubba(array):
    length = len(array)
    result = True
    global count
    while result:
        result = False
        i = 0
        while i < length - 1:
            if array[i] > array[i + 1]:
                tempVar = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tempVar
                result = True
            i = i + 1
            count += 1

    return array


count = 0
time1 = time.time()
arrayResult = str(bubba(input_array))
