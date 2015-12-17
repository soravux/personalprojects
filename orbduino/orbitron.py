import sys
import orbAPI
from multiprocessing import Process

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _Getch()

done = False
inp = None
spd = 230
while  not done:
    inp = getch()

    if inp == '+':
        spd += 230

    if inp == '-':
        spd -= 230

    if inp == '0':
        done = True

    if inp == 'a':
        Process(target=orbAPI.arm.base, args=(-spd,)).start()
    if inp == 'd':
        Process(target=orbAPI.arm.base, args=(spd,)).start()

    if inp == 'w':
        Process(target=orbAPI.arm.shoulder, args=(int(spd/1.5),)).start()
    if inp == 's':
        Process(target=orbAPI.arm.shoulder, args=(-spd,)).start()

    if inp == 'r':
        Process(target=orbAPI.arm.elbow, args=(spd,)).start()
    if inp == 'f':
        Process(target=orbAPI.arm.elbow, args=(-spd,)).start()

    if inp == 't':
        Process(target=orbAPI.arm.wrist, args=(spd,)).start()
    if inp == 'g':
        Process(target=orbAPI.arm.wrist, args=(-spd,)).start()

    if inp == 'q':
        Process(target=orbAPI.arm.pincher, args=(spd,)).start()
    if inp == 'e':
        Process(target=orbAPI.arm.pincher, args=(-spd,)).start()
