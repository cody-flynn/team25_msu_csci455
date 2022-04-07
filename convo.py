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

    def toString(self):
        return "{"+self.query+", "+self.response+", "+str(self.subrules)+", "+str(self.level)+"}"

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
    
    def bracketStrip(self, items, cnt):
        items=items.replace("[","").replace("]","").strip()
        st=-1
        ret=[]
        for i in range(int(cnt/2)):
            st=items.index("\"",st+1)
            en=items.index("\"",st+1)
            ret.append(items[st+1:en])   # append "string" without " to return list
            items=items[0:st]+items[en+1:] #remove "string"
        [ret.append(i) for i in items.split()]
        return ret
    
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

                if "~" == line[0]: # Is a definition line
                    c=line.split(":")
                    if len(c) != 2:
                        print("Syntax Error Definition: "+line)
                        continue
                    c[0]="$"+c[0].strip()[1:] # remove whitespace and leading ~, add $ var character
                    
                    if c[1].count("[") != 1:
                        print("Syntax Error: Missing \"[\":"+line)
                        continue
                    
                    if c[1].count("]") != 1:
                        print("Syntax Error: Missing \"]\":"+line)
                        continue

                    dqcnt=c[1].count("\"")
                    if dqcnt%2 == 1:
                        print("Syntax Error: Missing or extra \": "+line)
                        continue

                    self.variables[c[0]]=self.bracketStrip(c[1][c[1].index("["):c[1].index("]")],dqcnt)
                    continue

                c=line.split(":")
                if len(c) != 3:
                    print("Missing ':':" + line)
                    continue
                    
                # find the correct parent level to add to
                clevel=int("0"+c[0][1:])
                if (clevel < 0) or (clevel > (p.level + 1)): 
                    print("Invalid U level: " + line)
                    continue

                while p.level >= clevel: # while child level is bigger than parent
                    p=p.parent

                # filter the query, searching for "_"
                c[1]=c[1].replace("(","").replace(")","").strip()
                if "_" in c[1]:
                    if "$" not in c[2]: # if found, add new variable
                        print("Missing variable: " + line)
                        continue
                    self.variables[c[2][c[2].index("$"):].split()[0]] = "" # make empty variable

                c[2]=c[2].strip()
                bracketNum=c[2].count("[")
                if bracketNum > 0:
                    if bracketNum != c[2].count("]"):
                        print("Bad list: " + line)
                        continue
                    
                    # Take n bracket variables
                    st=-2
                    for i in range(bracketNum):
                        st=c[2].index("[",st+2) # 2 needed because we add $ before, incrementing all values
                        en=c[2].index("]",st+1)
                        print(st)
                        print(en)
                        tempBstr=c[2][st:en+1]
                        print(tempBstr)
                        tempNoSp=tempBstr.replace(" ","")
                        print(tempNoSp)
                        self.variables["$"+tempNoSp]=self.bracketStrip(tempBstr,tempBstr.count("\""))
                        c[2]=c[2][0:st]+"$"+tempNoSp+c[2][en+1:]

                # deal with _ variables in ask functiton
                p.subrules.append(QAPair(c[1],c[2],[],p,clevel))

                p=p.subrules[-1]

        return

    def ask(self, inp):
        pass
        # Modify the valid list each time this is called


# load in test file and test this class
def main():
    convo = Convo()

    convo.parse('testing.txt')

    x = ''
    while x != "bye":
        x = input("Human: ")
        convo.ask(x)
#main()
