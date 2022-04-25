from conversation import Conversation
from tangoBot import TangoBot
from gui import GUI
import speech_recognition as sr 

def main():

    mybot = TangoBot()
    #import keyboard
    #command = None
    #while True:
    #    event = keyboard.read_event()
    #    if event.event_type == keyboard.KEY_DOWN:
    #        key = event.name
    #        mybot.command(key)
    #        if key == '0':

     
    mydict={"go forward"    : 'w',
            "go back"       : 's',
            "go left"       : 'a',
            "go right"      : 'd',
            "look left"     : 'j',
            "look right"    : 'l',
            "look up"       : 'i',
            "look down"     : 'k',
            "turn left"     : 'z',
            "turn right"    : 'c',
            "stop"          : 'x'}
    gui=GUI()
    gui.run()
    c=""
    while c != "bye":
        if gui.list_valid:
            x = gui.get_response()
            for command in x:
                command.lower()
                command.strip(' ')
                print(command) 
                if command in mydict.keys():
                    mybot.command(mydict[command])
                if command == "bye":
                    c = "bye"
            gui.run()


# load in test file and test this class                                                                             
    #convo = Convo()
    #convo.parse('testing.txt')

    #x = ''
    #child_rules = []
    #while x != "bye":
    #    x = input("Human: ").lower()
    #    child_rules = convo.ask(x, child_rules)
    #    print("Robot: " + convo.response_string)
    
    #listening = True 
    #while listening: 
    #    with sr.Microphone() as source: 
    #        r= sr.Recognizer() 
    #        r.adjust_for_ambient_noise(source) 
    #        r.dyanmic_energythreshhold = 3000 
    #         
    #        try: 
    #            print("listening") 
    #            audio = r.listen(source)             
    #            print("Got audio") 
    #            command = r.recognize_google(audio)
    #            command.lower()
    #            command.strip(' ')
    #            print(command) 
    #            if command in mydict.keys():
    #                mybot.command(mydict[command])
    #        except sr.UnknownValueError: 
    #            print("Don't knoe that werd") 

main()

