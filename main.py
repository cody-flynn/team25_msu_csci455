class TangoBot:
    # These are the main movement controls
    def move_forward():
        print("move forward")
        return

    def move_left():
        print("turn left")
        return

    def reverse():
        print("moving in reverse")
        return

    def move_right():
        print("turn right")
        return

    # head pan controls
    def head_pan_left():
        print("pan head left")
        return

    def head_pan_right():
        print("pan head right")
        return

    def head_pan_up():
        print("pan head up")
        return

    def head_pan_down():
        print("pan head down")
        return

    # waist turn controls
    def waist_turn_right():
        print("turn waist right")
        return

    def waist_turn_left():
        print("turn waist left")
        return

    # arm controls
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
                reverse()
            elif command == 'd':
                move_right()
            elif command == 'z':
                waist_turn_left()
            elif command == 'c':
                waist_turn_right()
            elif command == 'i':
                head_pan_up()
            elif command == 'j':
                head_pan_left()
            elif command == 'k':
                head_pan_down()
            elif command == 'l':
                head_pan_right()
            else:
                continue
        print("goodbye")




