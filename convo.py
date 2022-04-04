# This class creates the data structure of answers/subanswers
class Dialogue:
    question=None # question to respond to
    response=None # answer to the question, array for multiple options
    subrules=None # Array of more sub-dialogue options
    pass

class Convo:
    responses=None #list of listparsed U responses
    valid=None #list of valid responses

    def parse(self, inp):
        # add in string parsing, remove whitespace, tolower, etc
        pass

    def ask(self,inp):
        passd
        # Modify the valid list each time this is called

# load in test file and test this class

