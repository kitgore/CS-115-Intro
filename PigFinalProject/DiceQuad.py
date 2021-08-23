from Die import Die

class DiceQuad():

    def __init__(self):
        '''Initilizes dieList as a list of 4 Die objects
        To create a die object, call Die()'''
        #DONE
        d1 = Die()
        d2 = Die()
        d3 = Die()
        d4 = Die()
        self.dieList = [d1, d2, d3, d4]

    def roll(self):
        '''Rolls all four dice in dieList'''
        #DONE
        for i in range(len(self.dieList)):
            self.dieList[i].roll()

    def num1s(self):
        '''return the number of ones rolled'''
        #DONE
        count = 0
        for i in range(len(self.dieList)):
            if self.dieList[i].getFaceValue() == 1:
                count += 1
        return count

    
    
    def getDiceTotal(self):
        '''return the sum of the dice'''
        #DONE
        sum = 0
        for i in range(len(self.dieList)):
            sum += self.dieList[i].getFaceValue()
        return sum

    def __str__(self):
        '''String representation of the dice roll'''
        s = "("+str(self.dieList[0])
        for x in range(1, len(self.dieList)):
            s = s+","+str(self.dieList[x])
        s = s+")"
        return s
