
# Given an array rotates the values clockwise by one, the last value is sent to the first position.
# for more information look at the examples


def rotatebyOne(arr):
    last_el = arr.pop()
    arr.insert(0, last_el)
    return arr


print(rotatebyOne([6, 5, 8, 9, 7]))
