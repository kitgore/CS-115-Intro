
#Benjamin Griepp
#10/2/2020
#I pledge my honor that I have abided by the Stevens Honor System.


def dotProduct(L, K):
    #takes in L and K, multiplies first terms of each and then adds it with a recursive call without the first terms until the lists are empty, returning the sum
    if not (L and K):
        return 0
    return((L[0] * K[0]) + dotProduct(L[1:], K[1:]))

def expand(S):
    #returns a list object of the first character plus a call of the function without the first object
    if S == [] or S == "":
        return []
    else:
        return [S[0]] + expand(S[1:])

def deepMember(e, L):
    #checks if 1st list element is equal to e, returning true if equal, and continuing recursively without 1st element if not equal
    #if object is list, applies function to just list
    if L == []:
        return False
    elif isinstance(L[0], list):
        if(True == deepMember(e, L[0])):
            return True
        else:
            return deepMember(e, L[1:])
    else:
        if L[0] == e:
            return True
        else:
            return deepMember(e, L[1:])


def removeAll(e, L):
    #if 1st L element is equal to e, continues a call function without 1st element, if not equal adds element to another call function without 1st element
    if L == []:
        return []
    else:
        if L[0] == e:
            return removeAll(e, L[1:])
        else:
            return [L[0]] + removeAll(e, L[1:])


def deepReverse(L):
    #calls the function without the first element of list and adds the first element to end of list until gone through all list objects
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]
