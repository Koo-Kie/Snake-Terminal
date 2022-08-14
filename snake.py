import subprocess, time, threading
import keyboard as kb
from time import sleep
from termcolor import colored

subprocess.call("clear", shell=True)
subprocess.call("stty -echo", shell=True)
def menu():
    print('''
      /$$$$$$                      /$$
     /$$__  $$                    | $$
    | $$  \__/ /$$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$
    |  $$$$$$ | $$__  $$ |____  $$| $$  /$$/ /$$__  $$
     \____  $$| $$  \ $$  /$$$$$$$| $$$$$$/ | $$$$$$$$
     /$$  \ $$| $$  | $$ /$$__  $$| $$_  $$ | $$_____/
    |  $$$$$$/| $$  | $$|  $$$$$$$| $$ \  $$|  $$$$$$$
     \______/ |__/  |__/ \_______/|__/  \__/ \_______/
    ''')
    print('\n----------------------------')
    print('\nBy Kookie\n')
    print('----------------------------')
    print(colored('\nPress space to start', 'white', attrs=['bold']))
    kb.wait('space')
    subprocess.call('clear', shell=True)
menu()
# map loader
map = []
print(' _______________________________________________')
for i in range(15):
    print('|', end='')
    for b in range(15):
        print('  .', end='')
        map.append('.')
    print('  |\r')
    map.append('|')
print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

direction = ""
def generate_map():
    subprocess.call('clear', shell=True)
    print(' ______________________________________________')
    print('|', end='\b')
    for i in map:
        print('  '+i, end='')
        if i == '|':
            print('\r|')
    print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

co = [3,14]
def converter(co, char):
    indices = [index for index, element in enumerate(map) if element == "|"]
    # co = input("\nCo: ").split(",")
    if co[1] == 1:
        map[co[0]-2] = "."
        map[co[0]-1] = char
    elif co[1] != '1':
        map[int(indices[co[1]-2])+ co[0]] = char
        if direction == 'up':
            map[int(indices[co[1]-1])+ co[0]] = "."
        elif direction == 'down':
            map[int(indices[co[1]-3])+ co[0]] = "."
        elif direction == 'right':
            map[int(indices[co[1]-2])+ co[0]-1] = "."
        elif direction == 'left':
            map[int(indices[co[1]-2])+ co[0]+1] = "."

    generate_map()

# direction= []
direction = ''
def thread():
    global direction
    while True:
        # direction.append(kb.read_key())
        direction = kb.read_key()
        sleep(.4)

def movement():
        if direction == 'up':
            co[1]-= 1
        elif direction == 'down':
            co[1]+= 1
        elif direction == 'right':
            co[0]+= 1
        elif direction == 'left':
            co[0]-= 1

if __name__ =="__main__":
    t1 = threading.Thread(target=thread)
    t1.start()

    while True:
        # try:
        #     if direction[-1] == 'left' or 'right' and direction[-2] == 'right' or 'left':
        #         continue
        #     elif direction[-1] == 'up' or 'down' and direction[-2] == 'down' or 'up':
        #         continue
        #     movement()
        # except:
        #     pass
        movement()
        converter(co, '0')
        if co.count(0) or co.count(16) >= 1:
            break
        print(co)
        print(direction)
        sleep(0.5)
