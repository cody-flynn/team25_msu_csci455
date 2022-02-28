class TangoBot:
    # These are the main movement controls
    usb=None
    waist=None
    headv=None
    headh=None
    motor1=None
    motor2=None
    def __init__(self):
        import serial, time, sys, keyboard
        try:
            self.usb = serial.Serial('/dev/ttyACM0')
            print(self.usb.name)
            print(self.usb.baudrate)
        
        except:
            try:
                self.usb = serial.Serial('/dev/ttyACM1')
                print(self.usb.name)
                print(self.usb.baudrate)
            except:
                print("No servo serial ports found")
                sys.exit(0);
        self.waist=5800
        self.waist_turn()
        time.sleep(0.2)
        self.headv=5400
        self.head_virtical()
        time.sleep(0.2)
        self.headh=5900
        self.head_horizontal()
        time.sleep(0.2)
        self.motor1=7000
        #self.head_horizontal()
        #time.sleep(0.2)
        self.motor2=7000
        #self.head_horizontal()
        #time.sleep(0.2)

    def move_forward(self):
        self.motor1+=200;
        self.send(self.motor1,0x00);

    def send(self,target,dev):
        lsb = target &0x7F
        msb = (target >> 7) & 0x7F
        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(dev) + chr(lsb) + chr(msb)

        # Wait for last byte to send
        self.usb.flush()
        self.usb.write(cmd.encode('utf-8'))

    def move_left(self):
        self.motor2-=100;
        self.send(self.motor2,0x00);

    def reverse(self):
        self.motor1-=200;
        self.send(self.motor1,0x00);

    def move_right(self):
        self.motor2-=100;
        self.send(self.motor2,0x00);

    def rotate():
        print("rotate")
        return

    # head pan controls
    def head_pan_left(self):
        self.headh+=100
        self.head_horizontal()
        return

    def head_pan_right(self):
        self.headh-=100
        self.head_horizontal()
        return

    def head_horizontal(self):
        print("head l/r: " + str(self.headh))
        self.send(self.headh,0x03)

    def head_pan_up(self):
        print("pan head up")
        self.headv+=100
        self.head_virtical()

    def head_pan_down(self):
        print("pan head down")
        self.headv-=100
        self.head_virtical()

    def head_virtical(self):
        print("head u/d: " + str(self.headv))
        self.send(self.headv,0x04)

    # waist turn controls
    def waist_turn_right(self):
        print("turn waist right")
        self.waist+=200
        self.waist_turn()

    def waist_turn_left(self):
        print("turn waist left")
        self.waist-=200
        self.waist_turn()
        return

    def waist_turn(self):
        self.send(self.waist,0x02)

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

    def command(self, command):
        #if __name__ == '__main__':
        #command = 1
        #while command != '0':
        #print('Enter command:')
        #command = input()
        if command == 'w':
            self.move_forward()
        elif command == 'a':
            self.move_left()
        elif command == 's':
            self.reverse()
        elif command == 'd':
            self.move_right()
        #elif command == 'f':
            #self.rotate()
        elif command == 'z':
            self.waist_turn_left()
        elif command == 'c':
            self.waist_turn_right()
        #elif command == 'x':
            #self.waist_turn()
        elif command == 'i':
            self.head_pan_up()
        elif command == 'j':
            self.head_pan_left()
        elif command == 'k':
            self.head_pan_down()
        elif command == 'l':
            self.head_pan_right()
        else:
            pass
        #print("goodbye")
###############
###############
import keyboard
mybot = TangoBot()
command = None
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        mybot.command(key)
        if key == '0':
            break
