#!/bin/bash

rm -fr midiutil
mkdir midiutil

git clone git@github.com:MarkCWirt/MIDIUtil.git midiutil-clone

cp midiutil-clone/src/midiutil/MidiFile.py pyeuclid/midifile.py
rm -fr midiutil-clone

