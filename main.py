# set up list for testing
testList001 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def binary_search_001(num_list, lookupValue):
    ub = 0
    lb = len(num_list)-1
    run_search = True
    while run_search:
        midpoint = int(ub+lb/2)
        if lookupValue == midpoint:
            return True
        elif lookupValue > midpoint:
            ub = midpoint
            print("it's higher")
        elif lookupValue < midpoint:
            lb = midpoint
            print("it's lower")
        else:
            return False

# first test
found = binary_search_001(testList001, 8)
print(found)
