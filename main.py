# set up list for testing
testList001 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


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
# all it does is infinitely loop


# we will now retry after further explanation from Mr. M
def binary_search_002(num_list, lookupValue):
    found = False
    searchFailed = False
    LB = 0
    UB = len(num_list)-1
    while not found and not searchFailed:
        MP = int(LB+UB/2)
        # ahhhh, that's where it went wrong - order of operations.
        if num_list[MP] == lookupValue:
            found = True
        else:
            if UB-LB <= 1:
                searchFailed = True
            else:
                if num_list[MP] > lookupValue:
                    MP -= 1
                else:
                    MP += 1

def binary_search_003(num_list, searchItem):
    found = False
    searchFailed = False
    lowerBoundry = 0
    upperBoundry = len(num_list)-1
    while not found and not searchFailed:
        middle = int((lowerBoundry+upperBoundry)/2)
        if num_list[middle] == searchItem:
            found = True
        else:
            if lowerBoundry >= upperBoundry: # no search area left
                searchFailed = True
            else:
                if num_list[middle] > searchItem:
                    upperBoundry = middle-1
                else:
                    lowerBoundry = middle+1
    return found


# first test
found = binary_search_003(testList001, 5)
print(found)
