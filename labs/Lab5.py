####################################################################################
# Name: Benjamin Griepp
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################

# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
   #stores remainder bit and then calls function recursively dividing by 2 without remainder
   if x == 0:
      return [0]
   if x == 1:
      return [1]
   return [x%2] + decimalToBinary(x//2)



# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
   #takes first number out of list adds first number to the sum then multiplies remaining list by 2 
   if num == [] or num == [0]:
      return 0
   return num[0] + binaryToDecimal(num[1:]) * 2

#print(binaryToDecimal([1, 0, 1, 1, 1, 0, 0, 1, 1]))

# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
   #if 1st number in list is 1, make number 0 then add to remaining list, if 1st number in list is 0, make number 1 and return the list
   if num == []:
      return [1]
   if num == [1]:
      return [0,1]
   if num[0] == 0:
      num[0] = 1
      return num
   else:
      return [0] + incrementBinary(num[1:])
   
#print(incrementBinary([1, 1, 1]))

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up


def addZero(num):
   return num + [0]

def makeEquals(num1, num2):
   if len(num1) >= len(num2):
      return num1
   else:
       return makeEquals(num1 + [0], num2)

def removeZeroes(num1):
   if num1 == []:
      return num1
   if num1[-1] == 0:
      return removeZeroes(num1[:-1])
   else:
      return num1
   
#print(list(makeEquals([1,0,1], [1,1,1,1,1,1])))

def addBinary(num1, num2):
   num1 = makeEquals(num1, num2)
   num2 = makeEquals(num2, num1)
   #make lists same length by adding zeros to the shorter list

   if num1 == []:
      return []
   #lists done adding, returns empty list

   if num1[0] + num2[0] == 1:
      return removeZeroes([1] + addBinary(num1[1:], num2[1:]))
   #if numbers add to 1, store 1 and move to rest of lists

   if num1[0] + num2[0] == 2:
      return removeZeroes([0] + addBinary(incrementBinary(num1[1:]), addZero(num2[1:])))
   #if numbers add to 2, store 0, increment remaining list
   
   else:
      return removeZeroes([0] + addBinary(num1[1:], num2[1:]))
   #numbers add to 0, store 0 and move to rest of lists

print(addBinary([1, 1, 1, 1], [0, 0, 1, 0, 0 ,0]))


print(list(removeZeroes([1,0,1,0,0,1,0,0,0])))