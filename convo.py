# This class creates the data structure of answers/subanswers
class QAPair:
    question=None # question to respond to
    response=None # answer to the question, array for multiple options
    subrules=None # Array of more sub-dialogue options
    parent=None
    def __init__(self, questionStr="", answerStr="", subrulesList=[], parentQA=None):
        question=questionStr
        response=answerStr
        subrules=subrulesList
        parent=parentQA

# This class contains methods to parse a file into a question/response data structure,
# and query that data structure with questions and keep record of valid reponses at
# any given time.
class Convo:
    responses=None #list of QA structures
    valid=None #list of valid questions/QA structures to respond to.

    def __init__(self):
        responses=[]
        valid=[]
    
    def parse(self, fileToParse):
        # add in string parsing, remove whitespace, tolower, etc
        with open(fileToParse) as f:
            cur=QAPair()
            p=["u"]
            for line in f:
                if "#" in line:
                    line=line[0:line.index("#")]
                line=line.strip().lower()
                if "~" in line:
                    pass # fill in later
                elif line == "":
                    continue #skip empty lines
                else:
                    c=line.split(":")
                    if len(c) != 3:
                        print("Error in:" + line)

        

    def ask(self, inp):
        pass
        # Modify the valid list each time this is called


# load in test file and test this class
convo = Convo()
lines = []
with open('testing.txt') as f:
    lines = f.readlines()

#for line in lines:
#    convo.parse(line)

x = ''
while x != "bye":
    x = input("Human: ")
    convo.ask(x)

