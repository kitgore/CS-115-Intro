from pigPlayer import PigPlayer


def wantsContinue(prompt):
    '''Checks if the response a user gives indicates they want to continue.
    assume the user has to give a Y to mean yes and N to mean no'''
    ans = input(prompt)
    out = False
    while ans != 'Y' and ans != 'N':
        ans = input(prompt)
    if ans == 'Y':
        out = True
    #print("" + prompt + " " + str(out))
    return out

class HumanPlayer(PigPlayer):
    
    def wantsHandOver(self):
        '''Asks a human player if they want to play again'''
        #DONE
        print("\tYour current score: " + str(self.getCurrentScore()))
        if self.AUTO_WIN_RECOGNITION_ON and (self.getCurrentScore() >= self.WINNING_SCORE):
            return True
        return not wantsContinue("\tRoll again? (Y/N): ")
