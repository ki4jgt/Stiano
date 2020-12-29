import pyglet
from pyglet.window import key

from time import sleep

window = pyglet.window.Window()

def trans(item):
    player = pyglet.media.Player()
    player.queue(pyglet.media.synthesis.Digitar(1.0, frequency=item))
    player.loop = True
    return player

matrix = [[61.7354, 65.4064, 73.4162, 82.4069, 87.3071, 97.9989, 110.000], [123.471, 130.813, 146.832, 164.814, 174.614, 195.998, 220.000], [246.942, 261.626, 293.665, 329.628, 349.228, 391.995, 440.000], [493.883, 523.251, 587.330, 659.255, 698.456, 783.991, 880.000]]

for i in range(len(matrix)):
    matrix[i] = [*map(trans, matrix[i])]

L_KEYS = [97, 119, 115, 101, 100, 114, 102]
R_KEYS = [117, 106, 105, 107, 111, 108, 112]

L_OCTAVE = 1
R_OCTAVE = 2

@window.event
def on_draw():
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    global L_OCTAVE, R_OCTAVE

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