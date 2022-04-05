# This class creates the data structure of answers/subanswers
class Dialogue:
    question=None # question to respond to
    response=None # answer to the question, array for multiple options
    subrules=None # Array of more sub-dialogue options
    
    def __init__(self, questionStr, answerStr="I'm broken!", subrulesList=[]):
        question=questionStr
        response=answerStr
        subrules=subrulesList

# This class contains methods to parse a file into a question/response data structure,
# and query that data structure with questions and keep record of valid reponses at
# any given time. 
class Convo:
    responses=None #list of Dialogue structures
    valid=None #list of valid questions/Dialogue structures to respond to.

    def __init__(self):
        pass

    def parse(self, inp):
        # add in string parsing, remove whitespace, tolower, etc
        pass

    def ask(self,inp):
        passd
        # Modify the valid list each time this is called

# load in test file and test this class

