''''
Created 12/11/2020 by David Treder
CS 115 - Final Pig Project Test Script Skeleton
'''

import unittest
import ComputerPlayer
import DiceQuad
import Die

D = Die.Die()
DQ = DiceQuad.DiceQuad()
C = ComputerPlayer.ComputerPlayer("dummy", "computer")
#NOTE: I initialize the owner as "dummy". This is not valid but we wont be using functions that use owner.

# =============================================
# INSTRUCTIONS:

# Complete the TODOs, and anything else you think is useful.
# Make sure you also test playing the program normally, this won't be able to test everything

class Test(unittest.TestCase):

# TESTING DIE
# Tests creating a die, rolling the die, setting the face of a die, getting the face of a die, string representation of die


    def test_init(self):
        #Check the die starts at 1
        self.assertEqual(D.getFaceValue(), 1)

    def test_roll(self):
        #DONE - Roll the die and assert that it returns the faceValue
        rolledValue = D.roll()
        self.assertEqual(rolledValue, D.getFaceValue())

    def test_set(self):
        #DONE - Set the face of the die and assert the faceValue properly updates
        #REMINDER - the given setFaceValue in Die.py has an error.
        #           Change faceValue > 0 and faceValue <= MAX
        #               to faceValue > 0 and faceValue <= self.MAX
        D.setFaceValue(4)
        self.assertEqual(4, D.getFaceValue())
    def test_str(self):
        #DONE - Set the face value of the die and assert that the string representation is correct
        #Should be similar to test_set
        D.setFaceValue(4)
        self.assertEqual("4", str(D))

#TESTING DICEQUAD
#Tests creating the Quad, rolling the quad, getting the number of 1s, and the sum of the dice

    def test_initQ(self):
        #Check the string representation of the initial state
        self.assertEqual(str(DQ), "(1,1,1,1)")

    def test_rollQ(self):
        #DONE - Roll the quad and assert the string representation is not the default state
        #NOTE:  Dice rolling is random, you may have rolled 4 1s by chance even if the program works.
        #If you fail only this test case, try again. It is very unlikely to happen twice in a row.

        DQ.roll()
        self.assertNotEqual(str(DQ), "(1,1,1,1)")

    def test_ones(self):
        #DONE - Check number of 1s
        #Don't worry about the loop, it just tests this one multiple times
        for i in range(40):
            DQ.roll()
            valList = list(map(lambda x: x.getFaceValue(), DQ.dieList))
            self.assertEqual(DQ.num1s(), valList.count(1))

    def test_total(self):
        #DONE - Check getDiceTotal returns sum of dice
        DQ.roll()
        valList = list(map(lambda x: x.getFaceValue(), DQ.dieList))
        self.assertEqual(DQ.getDiceTotal(), sum(valList))
        

# TESTING PLAYER
# Tests hasWon, resetting, getting the current score, and if the computer wants to continue
# Use ComputerPlayer to do all these tests


    def test_hasWon(self):
        C.reset()

        self.assertFalse(C.hasWon())

        #DONE - Update score to be above 100
        C.score = C.WINNING_SCORE

        self.assertTrue(C.hasWon())
        

    def test_reset(self):
        C.score = 5000
        C.roundScore = 50
        C.isPlayerTurn = True

        C.reset()
        
        #DONE - Check that above values are reset
        self.assertEqual(C.score, 0)
        self.assertEqual(C.roundScore, 0)
        self.assertFalse(C.isPlayerTurn)

    def test_curr_score(self):

        s = 400
        rs = 100

        #DONE - set the score to s
        C.score = s
        #DONE - assert that getCurrentScore returns s
        self.assertEqual(s, C.getCurrentScore())
        #DONE - set the roundscore to rs
        C.roundScore = rs
        #DONE - set isPlayerTurn to True
        C.isPlayerTurn = True
        #DONE - assert that getCurrentScore returns s+rs
        self.assertEqual(C.getCurrentScore(), rs+s)

    def test_wants_cont(self):
        C.reset()

        self.assertFalse(C.wantsHandOver())

        #DONE - set roundscore to be > target (20)
        C.roundScore = C.targetPointsPerRound + 1

        #DONE - assert that C.wantsHandOver() is True
        self.assertTrue(C.wantsHandOver())


if __name__ == "__main__":
    unittest.main()


