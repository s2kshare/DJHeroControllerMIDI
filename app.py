import pygame
import mido
from mido import Message

# ! BE SURE TO: Install loopMIDI and make a port name "DJHeroMIDI"
# ! BE SURE TO: Have a C++ Compiler for rtmidi
# TODO: Issues occur if said plugin is not detected (Controller Config)

# INITIALIZATION
pygame.init()
pygame.joystick.init()

# CONTROLLER CONFIGURATION MAPPING
# Axes
TURNTABLE_AXIS = 3

# Buttons
BUTTON_SQUARE = 0
BUTTON_CROSS = 1
BUTTON_CIRCLE = 2
BUTTON_TRIANGLE = 3
BUTTON_SELECT = 8
BUTTON_START = 9
BUTTON_PS = 12

# Hats
DIRECTIONAL_KEYS = 0

# Check if a Device is connected
if pygame.joystick.get_count() == 0:
    print("No joystick found. Exiting...")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Connect to FL Studio's MIDI port
    midi_out = mido.open_output("DJHeroMIDI 1")  # Use the correct loopMIDI port

    # Initialize previous button states
    prev_btn_state = {
        BUTTON_SQUARE: False,
        BUTTON_CROSS: False,
        BUTTON_CIRCLE: False,
        BUTTON_TRIANGLE: False,
        BUTTON_SELECT: False,
        BUTTON_START: False,
        BUTTON_PS: False
    }

    OFFSET = 24

    while True:
        # Process Events
        pygame.event.pump()

        # Variables for updates and while loop
        axis_turntable = joystick.get_axis(TURNTABLE_AXIS)
        BTN_SQUARE = joystick.get_button(BUTTON_SQUARE)
        BTN_CROSS = joystick.get_button(BUTTON_CROSS)
        BTN_CIRCLE = joystick.get_button(BUTTON_CIRCLE)
        BTN_TRIANGLE = joystick.get_button(BUTTON_TRIANGLE)
        BTN_SELECT = joystick.get_button(BUTTON_SELECT)
        BTN_START = joystick.get_button(BUTTON_START)
        BTN_PS = joystick.get_button(BUTTON_PS)

        # Message MIDI
        midi_turntable = int((axis_turntable + 1) * 63.5)

        if midi_turntable > 0.02 or midi_turntable < -0.02:
            # Send MIDI CC for Turntable
            midi_out.send(Message("control_change", control=1, value=midi_turntable))

        # Function to send MIDI for button presses
        def send_button_midi(note, current_state, prev_state):
            if current_state != prev_state:  # Check if button state changed
                if current_state:  # Pressed
                    midi_out.send(Message("note_on", note=note, velocity=127))
                else:  # Released
                    midi_out.send(Message("note_off", note=note, velocity=0))
                return current_state  # Update previous state
            return prev_state  # No state change, return the same

        # Assign MIDI notes for buttons and check state changes
        prev_btn_state[BUTTON_SQUARE] = send_button_midi((60 - OFFSET), BTN_SQUARE, prev_btn_state[BUTTON_SQUARE])
        prev_btn_state[BUTTON_CROSS] = send_button_midi((61 - OFFSET), BTN_CROSS, prev_btn_state[BUTTON_CROSS])
        prev_btn_state[BUTTON_CIRCLE] = send_button_midi((62 - OFFSET), BTN_CIRCLE, prev_btn_state[BUTTON_CIRCLE])
        prev_btn_state[BUTTON_TRIANGLE] = send_button_midi((64 - OFFSET), BTN_TRIANGLE, prev_btn_state[BUTTON_TRIANGLE])
        prev_btn_state[BUTTON_SELECT] = send_button_midi((65 - OFFSET), BTN_SELECT, prev_btn_state[BUTTON_SELECT])
        prev_btn_state[BUTTON_START] = send_button_midi((66 - OFFSET), BTN_START, prev_btn_state[BUTTON_START])
        
        # For the PS button, send a control change message with value 0 or 1
        if BTN_PS != prev_btn_state[BUTTON_PS]:  # If state changed
            if BTN_PS:  # Button held down
                midi_out.send(Message("control_change", control=2, value=127))  # Set value to 0
            else:  # Button released
                midi_out.send(Message("control_change", control=2, value=0))  # Set value to 1
        prev_btn_state[BUTTON_PS] = BTN_PS  # Update the previous state

        print(f"Square: {BTN_SQUARE}, Cross: {BTN_CROSS}, Circle: {BTN_CIRCLE}, Triangle: {BTN_TRIANGLE}, Select: {BTN_SELECT}, Start: {BTN_START}, PS: {BTN_PS}, Turntable: {axis_turntable}")

        pygame.time.wait(10)  # Avoid CPU overload
