#!/bin/bash

rm -fr midiutil
mkdir midiutil

git clone git@github.com:MarkCWirt/MIDIUtil.git midiutil-clone

cp midiutil-clone/src/midiutil/*.py midiutil
rm -fr midiutil-clone

