# This class creates the data structure of answers/subanswers
class QAPair:
    query=None # query to respond to
    response=None # answer to the query, array for multiple options
    subrules=None # Array of more sub-dialogue options
    parent=None
    level=None
    def __init__(self, _query="", _response="", _subrules=[], _parentQAPair=None, _level=0):
        self.query=_query
        self.response=_response
        self.subrules=_subrules
        self.parent=_parentQAPair
        self.level=_level

# This class contains methods to parse a file into a query/response data structure,
# and query that data structure with querys and keep record of valid reponses at
# any given time.
class Convo:
    rootNode=None
    valid=None #list of valid querys/QA structures to respond to.
    variables=None

    def __init__(self):
        self.rootNode=QAPair("Q","A",[],None,-1)
        self.valid=[]
        self.variables={}
    
    def parse(self, fileToParse):
        # add in string parsing, remove whitespace, tolower, etc
        with open(fileToParse) as f:
            p=self.rootNode
            for line in f:
                if "#" in line:
                    line=line[0:line.index("#")]
                line=line.strip().lower()

                if line == "":
                    continue #skip empty lines

                if "~" == line[0]:
                    pass # fill in later
                    continue

                c=line.split(":")
                if len(c) != 3:
                    print("Error in:" + line)
                    continue
                    
                # find the correct parent level to add to
                clevel=int("0"+c[0][1:])
                if (clevel < 0) or (clevel > (p.level + 1)): 
                    print("Invalid U level: " + line)
                while p.level >= clevel: # while child level is bigger than parent
                    p=p.parent

                # filter the query, searching for "_"
                c[1]=c[1].replace("(","").replace(")","").strip()
                if "_" in c[1] and "$" not in c[2]: # if found, add new variable
                    print("Missing variable: " + line)
                    continue

                c[2]=c[2].strip()
                bracketNum=c[2].count("[")
                if bracketNum != c[2].count("]"):
                    print("Bad list: " + line)
                    continue
                
                # Take n bracket variables
                #for i in bracketNum:
                #    c2list=

                # deal with _ variables in ask functiton
                p.subrules.append(QAPair(c[1],c[2],[],p,clevel))

                p=p.subrules[-1]

    def ask(self, inp):
        pass
        # Modify the valid list each time this is called


# load in test file and test this class
convo = Convo()

convo.parse('testing.txt')

x = ''
while x != "bye":
    x = input("Human: ")
    convo.ask(x)

