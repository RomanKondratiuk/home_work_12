def get(array, index, default=None):
    if index < 0:
        print(default)
    elif index not in range(len(array)):
        print(default)
    else:
        print(array[index])


get([1, 2, 3], 4, "test")