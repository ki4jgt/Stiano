import pyglet
from pyglet.window import key

from time import sleep

window = pyglet.window.Window()

def trans(item):
    player = pyglet.media.Player()
    player.queue(pyglet.media.synthesis.Digitar(1.0, frequency=item))
    player.loop = True
    return player

matrix = [[61.7354, 65.4064, 69.2957, 73.4162, 77.7817, 82.4069, 87.3071, 92.4986, 97.9989, 103.826, 110.000, 116.541],
            [123.471, 130.813, 138.591, 146.832, 155.563, 164.814, 174.614, 184.997, 195.998, 207.652, 220.000, 233.082],
            [246.942, 261.626, 277.183, 293.665, 311.127, 329.628, 349.228, 369.994, 391.995, 415.305, 440.000, 466.164],
            [493.883, 523.251, 554.365, 587.330, 622.254, 659.255, 698.456, 739.989, 783.991, 830.609, 880.000, 932.328]]

for i in range(len(matrix)):
    matrix[i] = [*map(trans, matrix[i])]

L_KEYS = [97, 119, 50, 115, 51, 101, 100, 52, 114, 53, 102, 49]
R_KEYS = [117, 106, 55, 105, 56, 107, 111, 57, 108, 48, 112, 54]

L_OCTAVE = 1
R_OCTAVE = 2

@window.event
def on_draw():
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    global L_OCTAVE, R_OCTAVE
    
    print(symbol)

    if symbol in L_KEYS:
        matrix[L_OCTAVE][L_KEYS.index(symbol)].seek(0)
        matrix[L_OCTAVE][L_KEYS.index(symbol)].play()

    if symbol in R_KEYS:
        matrix[R_OCTAVE][R_KEYS.index(symbol)].seek(0)
        matrix[R_OCTAVE][R_KEYS.index(symbol)].play()

    if symbol == key.C:
        L_OCTAVE -= 1

    if symbol == key.V:
        L_OCTAVE += 1

    if symbol == key.N:
        R_OCTAVE -= 1

    if symbol == key.M:
        R_OCTAVE += 1

@window.event
def on_key_release(symbol, modifiers):
    global L_OCTAVE, R_OCTAVE

    if symbol in L_KEYS:
        for i in range(4):
            matrix[i][L_KEYS.index(symbol)].pause()

    if symbol in R_KEYS:
        for i in range(4):
            matrix[i][R_KEYS.index(symbol)].pause()

    if symbol == key.C:
        L_OCTAVE += 1

    if symbol == key.V:
        L_OCTAVE -= 1

    if symbol == key.N:
        R_OCTAVE += 1

    if symbol == key.M:
        R_OCTAVE -= 1

pyglet.app.run()