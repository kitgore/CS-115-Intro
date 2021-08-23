from pigPlayer import PigPlayer

class ComputerPlayer(PigPlayer):


    def __init__(self, owner, name, target=20):
        PigPlayer.__init__(self, owner, name)
        self.targetPointsPerRound = target

    def wantsHandOver(self):
        '''Return boolean if the AI wants to end the round based on target'''
        #DONE
        if (self.roundScore < self.targetPointsPerRound) or (self.getCurrentScore() >= self.WINNING_SCORE):
            return False
        else:
            return True
