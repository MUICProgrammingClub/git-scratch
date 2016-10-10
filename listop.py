modes = {'mult': 1, 'add': 0, 'pack': None}

def balanceList(lst1, lst2, mode):
    diff = abs(len(lst1) - len(lst2))
    if len(lst1) > len(lst2):
        lst2  += ([modes[mode]] * (diff))
    elif len(lst2) > len(lst1):
        lst1  += ([modes[mode]] * (diff))
    return lst1, lst2

def addTwoList(lst1, lst2):
    new_lst1, new_lst2 = balanceList(lst1, lst2, 'add')
    return [x + y for x, y in zip(new_lst1, new_lst2)]

def multTwoList(lst1, lst2):
    new_lst1, new_lst2 = balanceList(lst1, lst2, 'mult')
    return [x * y for x, y in zip(new_lst1, new_lst2)]

def pack(lst1, lst2):
    new_lst1, new_lst2 = balanceList(lst1, lst2, 'pack')
    return [(x, y) for x, y in zip(new_lst1, new_lst2)]
