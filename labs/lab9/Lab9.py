# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Benjamin Griepp
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 div r3 r1 r2
03 jeqzn r3 6
04 write r1
05 halt
06 write r2
07 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
00 read r1
01 read r2
02 copy r4 r1
03 setn r3 1
04 jeqzn r2 11
05 sub r2 r2 r3
06 jgtzn r2 09
07 write r1
08 halt
09 mul r1 r1 r4
10 jumpn 05
11 write r3
12 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 setn r2 0
02 setn r3 1
03 jeqzn r1 13
04 addn r1 -1
05 add r2 r2 r3
06 jeqzn r1 11
07 add r3 r2 r3
08 addn r1 -1
09 jeqzn r1 13
10 jgtzn r1 4
11 write r3
12 halt
13 write r2
14 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


