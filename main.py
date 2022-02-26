class TangoBot:
    # These are the main movement controls    
    def drvForward(self):
        print("move forward")
        return
    
    
    def drvRotateLeft(self):
        print("turn left")
        return
    
    
    def drvBack(self):
        print("move backward")
        return
    
    
    def drvRotateRigth(self):
        print("turn right")
        return
    
    
    if __name__ == '__main__':
        command = 1
        while command != '0':
            print('Enter command:')
            command = input()
            if command == 'w':
                move_forward()
            elif command == 'a':
                move_left()
            elif command == 's':
                move_back()
            elif command == 'd':
                move_right()
            else:
                continue
        print("goodbye")


