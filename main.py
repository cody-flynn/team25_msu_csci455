
def move_forward():
    print("move forward")
    return


def move_left():
    print("turn left")
    return


def move_back():
    print("move backward")
    return


def move_right():
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


