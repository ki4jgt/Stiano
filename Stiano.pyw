#!/usr/bin/env python3

import pyglet
from pyglet.window import key

import mido

dev = mido.open_output("JT-4000 MICRO MIDI 1")

window = pyglet.window.Window()

def trans(item):
    player = pyglet.media.Player()
    player.queue(pyglet.media.synthesis.Digitar(1.0, frequency=item))
    player.loop = True
    return player

matrix = [[35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
            [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58],
            [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]]

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
        dev.send(mido.Message("note_on", note = matrix[L_OCTAVE][L_KEYS.index(symbol)]))

    if symbol in R_KEYS:
        dev.send(mido.Message("note_on", note = matrix[R_OCTAVE][R_KEYS.index(symbol)]))

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
            dev.send(mido.Message("note_off", note = matrix[i][L_KEYS.index(symbol)]))

    if symbol in R_KEYS:
        for i in range(4):
            dev.send(mido.Message("note_off", note = matrix[i][R_KEYS.index(symbol)]))

    if symbol == key.C:
        L_OCTAVE += 1

    if symbol == key.V:
        L_OCTAVE -= 1

    if symbol == key.N:
        R_OCTAVE += 1

    if symbol == key.M:
        R_OCTAVE -= 1

pyglet.app.run()