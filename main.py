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
    
    # These are the waist motor
    def waistTurn(self):
        pass

    # These are the head motors
    def headHorizontal(self):
        pass

    def headVertical(self):
        pass

    # these are the arm motors
    def arm1(self):
        pass
    def arm2(self):
        pass
    def arm3(self):
        pass
    def arm4(self):
        pass
    def arm5(self):
        pass
    def arm6(self):
        pass







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


