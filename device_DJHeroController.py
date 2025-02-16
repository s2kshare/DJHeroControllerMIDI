# name= DJ Hero Controller

"""
[[
	Surface:	DJ Hero Controller
	Developer:	s2kdevelopshare
	Version:	Beta 1.0
	Date:		14/2/2025
    Contact:	https://github.com/s2kshare
]]
"""

# ! To use this plugin, make sure you have a C++ compiler for rtmidi
# ! Navigate to C:\Documents\Image-Line\FL Studio\Settings\Hardware
# ! Create a folder named "DJ Hero Controller" Folder and put this file there

import device
import plugins
import midi

# CONFIGURATION
# Fruity Scratcher Input
MIXER_TRACK_INDEX = 6  # Change to track where Fruity Scratcher exists
SLOT_INDEX = 0  # Change to the Fruity Scratcher Slot
PARAM_INDEX = 0  # Adjust based on Fruity Scratcher's parameters

TURNTABLE_CC = 1  # MIDI Control Change number for the turntable (Found within base script)

def OnControlChange(event):
    if event.data1 == TURNTABLE_CC:
        # Get the current parameter value from Fruity Scratcher (normalized 0.0 to 1.0)
        current_value = plugins.getParamValue(PARAM_INDEX, MIXER_TRACK_INDEX, SLOT_INDEX)

        # Convert MIDI CC to a delta movement
        delta = (event.data2 - 64) / 128  # Normalize range (-1 to +1)

        # Apply incremental change
        new_value = max(0.0, min(1.0, current_value + delta))

        # Update the Fruity Scratcher parameter
        plugins.setParamValue(new_value, PARAM_INDEX, MIXER_TRACK_INDEX, SLOT_INDEX)

        # Mark event as handled
        event.handled = True