#HW 4: BRANCH RECURSION
#Benjamin Griepp
#I pledge my honor that I have abided by the Stevens Honor System.

#TASK 1

def change(amount, coins):
    if amount == 0:
        #error check
        return 0
    elif coins == [] or amount < 0:
        #error check
        return float('inf')
    elif coins[0] > amount:
        #coin can not be used for amount as too large
        return change(amount, coins[1:])
    else:
        lose = change(amount, coins[1:])
        #call function without first coin i.e "losing" coin

        use = change(amount - coins[0], coins) + 1
        #call function by subtracting current coin and adding a coin to the count i.e "using" coin

        return min(lose, use)
        #return minimum coins used of current lose and uses


#TASK 2

from random import randrange
#helper function for currency()
def duplicates(lst):
    #checks for duplicates in a list recursively
    if len(lst) <= 1:
        return False
    if lst[0] == lst[1]:
        return True
    if duplicates([lst[0]] + lst[2:]):
        return True
    if duplicates(lst[1:]):
        return True
    return False


def currency(length):
    #generates list of random values, if contains a duplicate, creates a new list, checks it etc
    blank = [0] * length
    coins = list(map(lambda x: x + randrange(100) + 1, blank))
    if duplicates(coins) == False:
        return coins
    else:
        #print(list(coins))
        return currency(length)

#MORE EFFICIENT CODE WITHOUT LAMBDA
"""
from random import randrange
#helper function for uniqList()
def duplicates(lst, num):
    #checks for duplicates in a list recursively
    if lst == []:
        return False
    elif lst[0] == num:
        return True
    else:
        return duplicates(lst[1:], num)

#helper function for currency
def uniqList(lst, length):
    if(len(lst) == length):
        return lst
    else:
        rand = randrange(20) + 1
        if duplicates(lst, rand):
            return(uniqList(lst, length))
        else:
            return uniqList(lst + [rand], length)

def currency(length):
   return uniqList([], length)
"""