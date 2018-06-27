#!/usr/bin/env python

from __future__ import print_function
import pytest

from pyeuclid.midifile import MIDIFile

class Test_MIDIFile(object):

    def test_cmajor_scale(self):
        degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
        track    = 0
        channel  = 9
        time     = 0    # In beats
        duration = 1    # In beats
        tempo    = 120   # In BPM
        volume   = 100  # 0-127, as per the MIDI standard
        
        MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created automatically)
        MyMIDI.addTempo(track, time, tempo)
        
        for i, pitch in enumerate(degrees):
            MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
            MyMIDI.addNote((track + 1), (channel - 1), pitch, time + i, duration, volume)
            
        with open("test_output/major-scale.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)
