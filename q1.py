def find_first(L, x):
    """Return the index of the first 
       occurrence of x in L"""
    if not isinstance(L, list):
        return False
    index = 0
    for item in L:
        if item == x:
            return index
        index = index + 1

x = 10
y = -5
M = [1, 2, 'three', 4 * x + y, 'thr' + 'e' * 2]

print(find_first(M, 'three'))