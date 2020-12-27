import pyglet
from pyglet.window import key

from time import sleep

window = pyglet.window.Window()

files = ["A-L", "A-R",
        "B-L", "B-R",
        "C-L", "C-R",
        "D-L", "D-R",
        "E-L", "E-R",
        "F-L", "F-R",
        "G-L", "G-R"]

L_PITCH = 1.0
R_PITCH = 1.0

L_KEYS = {}
R_KEYS = {}

for name in files:
    if name.find("-L") != -1:
        L_KEYS[name[0]] = pyglet.media.Player()
        L_KEYS[name[0]].queue(pyglet.resource.media(name + ".wav", streaming = False))
    else:
        R_KEYS[name[0]] = pyglet.media.Player()
        R_KEYS[name[0]].queue(pyglet.resource.media(name + ".wav", streaming = False))

@window.event
def on_draw():
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    global L_PITCH, R_PITCH, L_KEYS, R_KEYS

    if symbol == key.A:
        L_KEYS["B"].seek(0)
        L_KEYS["B"].play()

    if symbol == key.W:
        L_KEYS["C"].seek(0)
        L_KEYS["C"].play()

    if symbol == key.S:
        L_KEYS["D"].seek(0)
        L_KEYS["D"].play()

    if symbol == key.E:
        L_KEYS["E"].seek(0)
        L_KEYS["E"].play()

    if symbol == key.D:
        L_KEYS["F"].seek(0)
        L_KEYS["F"].play()

    if symbol == key.R:
        L_KEYS["G"].seek(0)
        L_KEYS["G"].play()

    if symbol == key.F:
        L_KEYS["A"].seek(0)
        L_KEYS["A"].play()

    if symbol == key.U:
        R_KEYS["B"].seek(0)
        R_KEYS["B"].play()

    if symbol == key.J:
        R_KEYS["C"].seek(0)
        R_KEYS["C"].play()

    if symbol == key.I:
        R_KEYS["D"].seek(0)
        R_KEYS["D"].play()

    if symbol == key.K:
        R_KEYS["E"].seek(0)
        R_KEYS["E"].play()

    if symbol == key.O:
        R_KEYS["F"].seek(0)
        R_KEYS["F"].play()

    if symbol == key.L:
        R_KEYS["G"].seek(0)
        R_KEYS["G"].play()

    if symbol == key.P:
        R_KEYS["A"].seek(0)
        R_KEYS["A"].play()

    if symbol == key.C:
        L_PITCH /= 2

    if symbol == key.V:
        L_PITCH *= 2

    if symbol == key.N:
        R_PITCH /= 2

    if symbol == key.M:
        R_PITCH *= 2

@window.event
def on_key_release(symbol, modifiers):
    global L_PITCH, R_PITCH, L_KEYS, R_KEYS

    if symbol == key.A:
        L_KEYS["B"].pause()

    if symbol == key.W:
        L_KEYS["C"].pause()

    if symbol == key.S:
        L_KEYS["D"].pause()

    if symbol == key.E:
        L_KEYS["E"].pause()

    if symbol == key.D:
        L_KEYS["F"].pause()

    if symbol == key.R:
        L_KEYS["G"].pause()

    if symbol == key.F:
        L_KEYS["A"].pause()

    if symbol == key.U:
        R_KEYS["B"].pause()

    if symbol == key.J:
        R_KEYS["C"].pause()

    if symbol == key.I:
        R_KEYS["D"].pause()

    if symbol == key.K:
        R_KEYS["E"].pause()

    if symbol == key.O:
        R_KEYS["F"].pause()

    if symbol == key.L:
        R_KEYS["G"].pause()

    if symbol == key.P:
        R_KEYS["A"].pause()

    if symbol == key.C:
        L_PITCH *= 2

    if symbol == key.V:
        L_PITCH /= 2

    if symbol == key.N:
        R_PITCH *= 2

    if symbol == key.M:
        R_PITCH /= 2

pyglet.app.run()