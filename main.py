from pynput.keyboard import*
from rich import print as rprint
from rich.console import Console
from rich.markdown import Markdown


import random
import pygame
pygame.init()

console = Console()

MARKDOWN ="""
# Welcome to MechFeel !
# build for people who do not have a Mechanical Keyboard
 """
MARKDOWNn ="""
# PROGRAM RUNNING ENJOY 😘😎
 """

md=Markdown(MARKDOWN)
md1=Markdown(MARKDOWNn)
console.print(md)





song= {
    "1": "q.wav",
    "2": "w.wav",
    "3": "e.wav",
    "4": "e.wav",
    "5": "r.wav",
    "6": "t.wav",
    "7": "y.wav",
    "8": "u.wav",
    "9": "i.wav",
    "10": "o.wav",
    "11": "p.wav",
    "12": "[.wav",
    "13": "].wav",
    "14": "backspace.wav",
    "15": "tab.wav",
    "16": "q.wav",
    "17": "w.wav",
    "18": "e.wav",
    "19": "r.wav",
    "20": "t.wav",
    "21": "y.wav",
    "22": "u.wav",
    "23": "i.wav",
    "24": "o.wav",
    "25": "p.wav",
    "26": "[.wav",
    "27": "].wav",
    "28": "enter.wav",
    "29": "tab.wav",
    "30": "a.wav",
    "31": "s.wav",
    "32": "d.wav",
    "33": "f.wav",
    "34": "g.wav",
    "35": "h.wav",
    "36": "j.wav",
    "37": "k.wav",
    "38": "l.wav",
    "39": "[.wav",
    "40": "].wav",
    "41": "q.wav",
    "42": "shift.wav",
    "43": "backspace.wav",
    "44": "z.wav",
    "45": "x.wav",
    "46": "c.wav",
    "47": "v.wav",
    "48": "b.wav",
    "49": "n.wav",
    "50": "m.wav",
    "51": "l.wav",
    "52": "[.wav",
    "53": "].wav",
    "54": "shift.wav",
    "55": "o.wav",
    "56": "e.wav",
    "57": "space.wav",
    "58": "caps lock.wav",
    "59": "w.wav",
    "60": "e.wav",
    "61": "e.wav",
    "62": "r.wav",
    "63": "t.wav",
    "64": "y.wav",
    "65": "u.wav",
    "66": "i.wav",
    "67": "o.wav",
    "68": "p.wav",
    "69": "u.wav",
    "70": "i.wav",
    "71": "y.wav",
    "72": "u.wav",
    "73": "i.wav",
    "74": "p.wav",
    "75": "h.wav",
    "76": "j.wav",
    "77": "k.wav",
    "78": "enter.wav",
    "79": "b.wav",
    "80": "n.wav",
    "81": "m.wav",
    "82": "shift.wav",
    "83": "[.wav",
    "87": "].wav",
    "88": "].wav"
}


path = ""

def press_new(key):
    # print('Press ON:{}'.format(key))
    # print( key)
    i = str(random.randint(1, 88))

    try:

        pygame.mixer.music.load(f'./Soundpacks/Soundpacks/nk-cream/{song[i]}')

    except Exception as e:
        print(e)
        pygame.mixer.music.load(f'./Soundpacks/Soundpacks/nk-cream/a.wav')

    pygame.mixer.music.play()
    if key == Key.esc:
        return False
   


def press_one(key):
    # print('Press ON:{}'.format(key))
    # print( key)
    i = str(random.randint(1, 88))

    try: 
    
        pygame.mixer.music.load(f'./Soundpacks/Soundpacks/cherrymx-{path}/{i}.ogg')
    
    except:
        print('error')
        pygame.mixer.music.load(f'./Soundpacks/Soundpacks/cherrymx-{path}/1.ogg')


    pygame.mixer.music.play()
    if key == Key.esc:
        return False

    

# //////////////////////////////////////////////////////////// /'/'/'/'/'/'/'/'
console.print("Enter 0 for Developer's Favourite  😍",style = "bold green")

console.print( 'Enter 1 for cherrymx-Black-abs 😁',style = "bold blue")
console.print( 'Enter 2 for cherrymx-Blue-abs 😁',style = "bold blue")
console.print( 'Enter 3 for cherrymx-Blue-pbt 😁',style = "bold blue")
console.print( 'Enter 4 for cherrymx-Brown-abs 😁',style = "bold blue")
console.print( 'Enter 5 for cherrymx-Red-pbt 😁',style = "bold blue")

console.print( '----- Press ESC anytime to exit ⛔------',style = "bold red")




inp = int(input('Enter Your Choice : '))
if(inp == 1):
    path = 'black-abs'
elif(inp == 2):
    path = 'blue-abs'
elif(inp == 3):
    path = 'blue-pbt'
elif(inp == 4):
    path = 'brown-abs'
elif(inp == 5):
    path = 'red-pbt'



if(inp == 0):

    with Listener(on_press=press_new)as listener:
        console.print(md1)
        listener.join()     

else:
    with Listener(on_press=press_one)as listener:
        console.print(md1)
        listener.join()     








