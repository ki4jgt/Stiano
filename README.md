# Play Like a Master Musician With Minimal Effort
## Glide from one octave to the next at the touch of a button!

Stiano is an open source midi controller (**SYNTH REQUIRED!**) which uses the ergonomic design of stenotype to help you effortlessly create music using nothing but a standard keyboard (NKRO preferred)! Stiano is designed to keep your 10 fingers at homerow, while offering you a full 4 scale (48 keys) layout. If you can type, you can play music with Stiano.

As a kid, I always wanted to play the piano. And though quite a few people were willing to tutor me, I could never manage to get to my lessons. Then my room started filling up with junk, and my free space got smaller and smaller. No space for a keyboard now!

Recently working as a professional stenographer, my dreams of becoming a master pianist had been placed on indefinite hold. . .

Until I found myself overworked, exhausted, and in desperate need of a creative outlet. But my home was just as cluttered as ever. I still didn't have any room for a keyboard. In a bout of frustration, I hobbled together two of the things I was most passionate about: stenotype and piano.

## Positioning

Stenotype uses a combination of finger positioning, shorthand, and short finger traveling to acheive typing speeds of ~300WPM. The benefits of transposing the piano to such a system are grossly apparent. There is a slight variance between stenotyping and normal typing though. Stenowriters place their fingers in the cracks between the homerow, and the next row up. And your thumbs should be located between the C,V and N,M keys. This position allows for better range of motion, easier access, and the possibility to press any combination of active keys you may need.

## Layout (EN-US)

Stiano's layout is quite simple to master: The Keyboard is split into two scales: The Left Scale, and The Right Scale (one for each hand). Each scale contains both C-Major and D-Minor (keys placed in-line for easier chord access).

Scales use the home row, the row above it, and the number keys. Each scale starts with B, and ends with A.

### Left Scale

**C-Major Left:*** WER (CEG)

***D-Minor Left:*** SDF (DFA)

Starting with the A key, we wrap around to W, and then descend to S. You can follow this wrap-and-descend motion all the way to the F key. This is the Left Hand Scale.

| Piano | Keyboard |
| ----- | -------- |
| **B** | A-KEY |
| **C** | W-KEY |
| **D** | S-KEY |
| **E** | E-KEY |
| **F** | D-KEY |
| **G** | R-KEY |
| **A** | F-KEY |

### Right Scale

**C-Major Right:*** JKL (CEG)

***D-Minor Right:*** IOP (DFA)

Starting with the U key, we descend to J, and then wrap around to I. You can follow this descend-and-wrap motion all the way to the P key. This is the Right Hand Scale.


| Piano | Keyboard |
| ----- | -------- |
| **B** | U-KEY |
| **C** | J-KEY |
| **D** | I-KEY |
| **E** | K-KEY |
| **F** | O-KEY |
| **G** | L-KEY |
| **A** | P-KEY |

### Sharps

The sharps are also divided by hand, and are accessible via the number row.
| **Left** |  |
| ------ | ----- |
| **A#** | 1-KEY |
| **C#** | 2-KEY |
| **D#** | 3-KEY |
| **F#** | 4-KEY |
| **G#** | 5-KEY |

| **Right** |  |
| ------ | ----- |
| **A#** | 6-KEY |
| **C#** | 7-KEY |
| **D#** | 8-KEY |
| **F#** | 9-KEY |
| **G#** | 0-KEY |

### Accessing other scales

Remember when I told you to keep your thumbs between C, V and N, M?

- Holding C takes your left hand down a scale.
- Holding V takes your left hand up a scale.

- Holding N takes your right hand down a scale.
- Holding M takes your right hand up a scale.

### Turning Pages

My ultimate goal with Stiano is to display sheet music onscreen. Q and ; are reserved exclusively for page turning.

## Requirements

Stiano requires the ```Pyglet``` and ```Mido``` Python libraries.

```pip install mido[ports-rtmidi] pyglet```

**Enjoy Stiano!**
