# DJ Hero Controller MIDI Integration

## Overview

This project enables a DJ Hero Controller (PS3 version) to send MIDI messages for FL Studio, allowing it to control parameters such as Fruity Scratcher or other MIDI-mapped functions. The script converts DirectInput signals into MIDI events using pygame and mido.

## Features

- Converts joystick input (axes, buttons) into MIDI messages.
- Sends MIDI signals to FL Studio via loopMIDI.
- Controls Fruity Scratcher using MIDI CC.
- Detects button presses/releases and sends appropriate MIDI notes.
- Allows real-time turntable manipulation.

## Prerequisites

### Software Requirements

- Python 3.x
- FL Studio (with Fruity Scratcher or any MIDI-mappable plugin)
- loopMIDI (to create a virtual MIDI port)
- C++ compiler (required for rtmidi)

### Python Dependencies

Install the required dependencies using:
`pip install requirements`

### Setup loopMIDI

1. Download & Install loopMIDI.
2. Create a new virtual MIDI port and name it "DJHeroMIDI".
3. Ensure FL Studio detects this MIDI port in Options > MIDI Settings.

# Installation & Usage

## 1. Running the Python Script

This script reads the DJ Hero Controller inputs and sends MIDI messages.

`python djhero_midi.py`

Ensure your controller is plugged in before running the script!

## 2. Configuring FL Studio

1. Navigate to: `C:\Documents\Image-Line\FL Studio\Settings\Hardware`
2. Create a folder named **"DJ Hero Controller"**.
3. Place the FL Studio script (**device_DJHeroController.py**) inside this folder.
4. Restart FL Studio and enable MIDI Input for "DJHeroMIDI" in settings.

# Controller Mapping

## Axes

| Control   | Joystick Axis | MIDI CC |
| --------- | ------------- | ------- |
| Turntable | Axis 3        | CC 1    |

## Buttons

| Button    | Joystick ID | MIDI Note |
| --------- | ----------- | --------- |
| Square    | 0           | 36        |
| Cross     | 1           | 37        |
| Circle    | 2           | 38        |
| Triangle  | 3           | 40        |
| Select    | 8           | 41        |
| Start     | 9           | 42        |
| PS Button | 12          | CC 2      |

# TODO:

- Implement a GUI to handle input configuration
- Map DPAD buttons
- Create executables
